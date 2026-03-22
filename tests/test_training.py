"""Tests for training configuration and utilities."""

import pytest
from pathlib import Path
import sys
import os

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

def test_training_config_loads():
    """Test that training config can be loaded."""
    try:
        import yaml
    except ImportError:
        pytest.skip("PyYAML not installed")
        return
    
    config_path = Path(__file__).parent.parent / 'configs' / 'train.default.yaml'
    assert config_path.exists(), "Training config file should exist"
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    assert 'model' in config, "Config should have model section"
    assert 'lora' in config, "Config should have lora section"
    assert 'training' in config, "Config should have training section"

def test_serve_config_loads():
    """Test that serving config can be loaded."""
    try:
        import yaml
    except ImportError:
        pytest.skip("PyYAML not installed")
        return
    
    config_path = Path(__file__).parent.parent / 'configs' / 'serve.default.yaml'
    assert config_path.exists(), "Serving config file should exist"
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    assert 'api' in config, "Config should have api section"
    assert 'retrieval' in config, "Config should have retrieval section"

def test_dry_run_env():
    """Test DRY_RUN environment variable handling."""
    try:
        from cm_expert.training.train_lora import get_config
    except ImportError:
        pytest.skip("Training module not available")
        return
    
    # Test with DRY_RUN=1
    os.environ['DRY_RUN'] = '1'
    config = get_config()
    assert config.dry_run == True, "DRY_RUN=1 should set dry_run to True"
    
    # Test with DRY_RUN=0
    os.environ['DRY_RUN'] = '0'
    config = get_config()
    assert config.dry_run == False, "DRY_RUN=0 should set dry_run to False"

def test_lora_config_structure():
    """Test LoRA config has required fields."""
    try:
        import yaml
    except ImportError:
        pytest.skip("PyYAML not installed")
        return
    
    config_path = Path(__file__).parent.parent / 'configs' / 'train.default.yaml'
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    lora = config.get('lora', {})
    required_fields = ['r', 'alpha', 'target_modules']
    
    for field in required_fields:
        assert field in lora, f"LoRA config should have {field}"
    
    # Validate r and alpha are positive integers
    assert lora['r'] > 0, "LoRA r should be positive"
    assert lora['alpha'] > 0, "LoRA alpha should be positive"

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
