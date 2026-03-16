"""
LoRA Fine-tuning Script for CondensAI.

Trains a base model (e.g., Mistral-7B, Qwen) on domain-specific condensed matter physics
data using LoRA (Parameter-Efficient Fine-Tuning).

Supports:
- Dry-run mode (validate config + dataset without GPU-heavy training)
- Full training with PEFT/LoRA
- Optional DAPT (Domain Adaptive Pre-Training) stage
"""

import argparse
import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

# Optional imports - gracefully degrade if not available
try:
    from transformers import (
        AutoTokenizer, AutoModelForCausalLM,
        TrainingArguments, TrainerCallback
    )
    from peft import LoraConfig, get_peft_model, TaskType
    from trl import SFTTrainer
    from datasets import load_dataset
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("[WARNING] transformers/peft/trl not available. Running in scaffold mode.")


def load_config(config_path: str) -> Dict[str, Any]:
    """Load YAML configuration."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def validate_dataset(train_file: str) -> bool:
    """Validate that the training dataset exists and is readable."""
    path = Path(train_file)
    if not path.exists():
        print(f"[ERROR] Training file not found: {train_file}")
        return False
    
    # Check if JSONL and has content
    try:
        with open(path, 'r', encoding='utf-8') as f:
            first_line = f.readline()
            if not first_line.strip():
                print(f"[ERROR] Training file is empty: {train_file}")
                return False
        print(f"[OK] Dataset validated: {train_file}")
        return True
    except Exception as e:
        print(f"[ERROR] Cannot read training file: {e}")
        return False


def train(config: Dict[str, Any]):
    """
    Main training function.
    
    Args:
        config: Training configuration dictionary
    """
    # Extract config values
    base_model = config.get('base_model', 'mistralai/Mistral-7B-Instruct-v0.3')
    train_file = config.get('train_file', './data/processed/sft.jsonl')
    output_dir = config.get('output_dir', './artifacts/lora-cmp')
    lora_config = config.get('lora', {})
    training_args = config.get('training', {})
    
    # Dry-run mode check
    dry_run = os.environ.get('DRY_RUN', '0') == '1'
    
    print("=" * 60)
    print("CondensAI: LoRA Training Configuration")
    print("=" * 60)
    print(f"Base Model: {base_model}")
    print(f"Training File: {train_file}")
    print(f"Output Directory: {output_dir}")
    print(f"Dry Run: {dry_run}")
    print(f"LoRA Config: r={lora_config.get('r', 32)}, alpha={lora_config.get('alpha', 64)}")
    print(f"Training Args: epochs={training_args.get('epochs', 3)}, lr={training_args.get('lr', 2e-4)}")
    print("=" * 60)
    
    # Step 1: Validate dataset
    if not validate_dataset(train_file):
        print("\n[ABORT] Dataset validation failed. Please ensure:")
        print("  1. Training file exists at specified path")
        print("  2. File is in JSONL format with 'text' or 'messages' field")
        print("  3. File is not empty")
        return False
    
    # If dry run, stop here
    if dry_run:
        print("\n[DRY RUN] Configuration and dataset validated successfully.")
        print("Set DRY_RUN=0 or remove DRY_RUN env var to run full training.")
        return True
    
    # Check dependencies
    if not TRANSFORMERS_AVAILABLE:
        print("\n[ERROR] Full training requires: transformers, peft, trl, datasets")
        print("Install with: pip install transformers peft trl datasets accelerate")
        return False
    
    # Check GPU
    try:
        import torch
        cuda_available = torch.cuda.is_available()
        if not cuda_available:
            print("\n[WARNING] CUDA not available. Training will be very slow on CPU.")
    except ImportError:
        print("\n[WARNING] torch not available. Cannot check GPU status.")
        cuda_available = False
    
    # Step 2: Load tokenizer and model
    print("\nLoading tokenizer and model...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(base_model)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        
        model = AutoModelForCausalLM.from_pretrained(
            base_model,
            torch_dtype=torch.float16 if cuda_available else torch.float32,
            device_map="auto" if cuda_available else None,
            trust_remote_code=True
        )
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        print("Make sure you have HuggingFace Hub login (huggingface-cli login)")
        return False
    
    # Step 3: Configure LoRA
    print("\nConfiguring LoRA adapters...")
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=lora_config.get('r', 32),
        alpha=lora_config.get('alpha', 64),
        lora_dropout=lora_config.get('dropout', 0.05),
        target_modules=lora_config.get('target_modules', ['q_proj', 'v_proj', 'k_proj', 'o_proj']),
        bias="none",
        inference_mode=False
    )
    
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    
    # Step 4: Load dataset
    print("\nLoading dataset...")
    try:
        dataset = load_dataset('json', data_files=train_file, split='train')
        print(f"Loaded {len(dataset)} examples")
    except Exception as e:
        print(f"[ERROR] Failed to load dataset: {e}")
        return False
    
    # Step 5: Training arguments
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    training_kwargs = {
        'output_dir': str(output_path),
        'num_train_epochs': training_args.get('epochs', 3),
        'per_device_train_batch_size': training_args.get('batch_size', 2),
        'gradient_accumulation_steps': training_args.get('grad_accum', 16),
        'learning_rate': training_args.get('lr', 2e-4),
        'max_seq_length': training_args.get('max_length', 4096),
        'logging_steps': 10,
        'save_steps': 100,
        'save_total_limit': 2,
        'fp16': cuda_available,
        'report_to': 'none',
    }
    
    args = TrainingArguments(**training_kwargs)
    
    # Step 6: Train
    print("\nStarting training...")
    trainer = SFTTrainer(
        model=model,
        args=args,
        train_dataset=dataset,
        tokenizer=tokenizer,
        dataset_text_field='text',  # or use 'messages' if using chat format
    )
    
    trainer.train()
    
    # Step 7: Save
    print("\nSaving LoRA adapter...")
    model.save_pretrained(output_path)
    tokenizer.save_pretrained(output_path)
    
    print(f"\n[SUCCESS] Training complete. Adapter saved to: {output_path}")
    print("To use: load with peft.PeftModel.from_pretrained(base_model, output_path)")
    return True


def main():
    parser = argparse.ArgumentParser(description='Train LoRA adapter for CondensAI')
    parser.add_argument('--config', type=str, default='configs/train.default.yaml',
                        help='Path to training config YAML')
    args = parser.parse_args()
    
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"[ERROR] Config file not found: {config_path}")
        print("Creating default config at", config_path)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        default_config = {
            'base_model': 'mistralai/Mistral-7B-Instruct-v0.3',
            'train_file': './data/processed/sft.jsonl',
            'output_dir': './artifacts/lora-cmp',
            'lora': {
                'r': 32,
                'alpha': 64,
                'dropout': 0.05,
                'target_modules': ['q_proj', 'v_proj', 'k_proj', 'o_proj']
            },
            'training': {
                'epochs': 3,
                'lr': 2e-4,
                'batch_size': 2,
                'grad_accum': 16,
                'max_length': 4096
            }
        }
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(default_config, f, default_flow_style=False)
        config = default_config
    else:
        config = load_config(str(config_path))
    
    success = train(config)
    exit(0 if success else 1)


if __name__ == '__main__':
    main()
