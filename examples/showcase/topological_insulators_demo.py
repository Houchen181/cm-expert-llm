"""
Topological Insulators Q&A Demo

This example demonstrates cm-expert-llm answering questions about topological phases
of matter, including topological insulators, Weyl semimetals, and quantum Hall effects.

Run with:
    python examples/showcase/topological_insulators_demo.py
"""

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.cm_expert.serve.api import CMExpertAPI

def main():
    """Demo: Topological phases Q&A with citations"""
    
    # Initialize API
    api = CMExpertAPI(config_path="configs/serve.default.yaml")
    
    # Example questions about topological materials
    questions = [
        {
            "question": "What is a topological insulator and how does it differ from a conventional insulator?",
            "context": "topology"
        },
        {
            "question": "Explain the concept of Z2 topological invariant. How is it calculated?",
            "context": "topology"
        },
        {
            "question": "What are the surface states of a 3D topological insulator?",
            "context": "topology"
        },
        {
            "question": "How do Weyl semimetals differ from topological insulators?",
            "context": "topology"
        },
        {
            "question": "What is the quantum spin Hall effect and its relation to topological insulators?",
            "context": "topology"
        }
    ]
    
    print("=" * 80)
    print("Topological Insulators Q&A Demo - cm-expert-llm")
    print("=" * 80)
    print()
    
    for i, qa in enumerate(questions, 1):
        print(f"Question {i}: {qa['question']}")
        print("-" * 80)
        
        print(f"Context: {qa['context']}")
        print("Answer: [Would be generated with citations from training data]")
        print()
        
        example_answer = """
Example answer structure:
- Definition and key properties
- Topological protection mechanism
- Band structure explanation
- Experimental signatures
- Citations to seminal papers (e.g., Kane-Mele, Bernevig-Zhang)
        """.strip()
        print(example_answer)
        print()
        print()

if __name__ == "__main__":
    main()
