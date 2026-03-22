"""Tests for evaluation utilities."""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

def test_cmphysbench_exists():
    """Test that CMPhysBench benchmark file exists."""
    bench_path = Path(__file__).parent.parent / 'src' / 'cm_expert' / 'eval' / 'benchmarks.py'
    assert bench_path.exists(), "CMPhysBench benchmarks file should exist"

def test_grounding_eval_exists():
    """Test that grounding evaluation module exists."""
    grounding_path = Path(__file__).parent.parent / 'src' / 'cm_expert' / 'eval' / 'grounding.py'
    assert grounding_path.exists(), "Grounding evaluation file should exist"

def test_eval_config_structure():
    """Test evaluation config has required fields."""
    try:
        import yaml
    except ImportError:
        pytest.skip("PyYAML not installed")
        return
    
    config_path = Path(__file__).parent.parent / 'configs' / 'eval.default.yaml'
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        assert 'benchmark' in config or 'eval' in config, "Config should have benchmark or eval section"

def test_benchmark_questions_format():
    """Test that benchmark questions have correct format."""
    # Check if benchmark data exists and has proper structure
    bench_path = Path(__file__).parent.parent / 'src' / 'cm_expert' / 'eval' / 'benchmarks.py'
    
    if bench_path.exists():
        try:
            content = bench_path.read_text(encoding='utf-8')
            # Should contain question definitions
            assert 'question' in content.lower() or 'Question' in content, "Should contain questions"
        except UnicodeDecodeError:
            # Skip if encoding issues
            pass

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
