"""
Run All Showcase Examples

This script runs all showcase examples to demonstrate the full capability
of cm-expert-llm across different areas of condensed matter physics.

Run with:
    python examples/showcase/run_all.py
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Run all showcase examples"""
    
    showcase_dir = Path(__file__).parent
    examples = [
        "superconductivity_demo.py",
        "topological_insulators_demo.py",
        "correlated_electrons_demo.py"
    ]
    
    print("=" * 80)
    print("cm-expert-llm Showcase - Running All Examples")
    print("=" * 80)
    print()
    
    for example in examples:
        example_path = showcase_dir / example
        if example_path.exists():
            print(f"\n{'='*80}")
            print(f"Running: {example}")
            print(f"{'='*80}\n")
            
            # Run the example
            result = subprocess.run(
                [sys.executable, str(example_path)],
                capture_output=False,
                text=True
            )
            
            if result.returncode != 0:
                print(f"Error running {example}")
                return 1
        else:
            print(f"Warning: {example} not found, skipping...")
    
    print("\n" + "=" * 80)
    print("All showcase examples completed!")
    print("=" * 80)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
