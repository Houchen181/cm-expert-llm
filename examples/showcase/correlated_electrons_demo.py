"""
Correlated Electrons Q&A Demo

This example demonstrates cm-expert-llm answering questions about strongly correlated
electron systems, including Mott insulators, quantum spin liquids, and heavy fermions.

Run with:
    python examples/showcase/correlated_electrons_demo.py
"""

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.cm_expert.serve.api import CMExpertAPI

def main():
    """Demo: Correlated electron systems Q&A with citations"""
    
    # Initialize API
    api = CMExpertAPI(config_path="configs/serve.default.yaml")
    
    # Example questions about correlated systems
    questions = [
        {
            "question": "What is the Hubbard model and why is it important for correlated electrons?",
            "context": "correlated"
        },
        {
            "question": "Explain the Mott metal-insulator transition. How does it differ from a band insulator?",
            "context": "correlated"
        },
        {
            "question": "What is a quantum spin liquid and how is it different from conventional magnetic ordering?",
            "context": "correlated"
        },
        {
            "question": "What are heavy fermion systems and what causes the large effective mass?",
            "context": "correlated"
        },
        {
            "question": "How does the Kondo effect manifest in metals with magnetic impurities?",
            "context": "correlated"
        }
    ]
    
    print("=" * 80)
    print("Correlated Electrons Q&A Demo - cm-expert-llm")
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
- Physical phenomenon explanation
- Key Hamiltonian/model
- Phase diagram discussion
- Experimental observations
- Citations to key papers (e.g., Hubbard, Anderson, Kondo)
        """.strip()
        print(example_answer)
        print()
        print()

if __name__ == "__main__":
    main()
