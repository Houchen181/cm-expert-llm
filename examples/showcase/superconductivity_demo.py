"""
Superconductivity Q&A Demo

This example demonstrates how cm-expert-llm answers questions about superconductivity
using retrieval-augmented generation from real physics papers and textbooks.

Run with:
    python examples/showcase/superconductivity_demo.py
"""

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.cm_expert.serve.api import CMExpertAPI

def main():
    """Demo: Superconductivity Q&A with citations"""
    
    # Initialize API (dry-run mode for demo)
    api = CMExpertAPI(config_path="configs/serve.default.yaml")
    
    # Example questions about superconductivity
    questions = [
        {
            "question": "What is the Meissner effect and how does it relate to perfect diamagnetism?",
            "context": "superconductivity"
        },
        {
            "question": "Explain the BCS theory of superconductivity. How do Cooper pairs form?",
            "context": "superconductivity"
        },
        {
            "question": "What is the difference between Type I and Type II superconductors?",
            "context": "superconductivity"
        },
        {
            "question": "How does the critical temperature (Tc) depend on material properties?",
            "context": "superconductivity"
        },
        {
            "question": "What are high-temperature superconductors and how do they differ from conventional superconductors?",
            "context": "superconductivity"
        }
    ]
    
    print("=" * 80)
    print("Superconductivity Q&A Demo - cm-expert-llm")
    print("=" * 80)
    print()
    
    for i, qa in enumerate(questions, 1):
        print(f"Question {i}: {qa['question']}")
        print("-" * 80)
        
        # In production, this would call the API
        # response = api.query(qa['question'], context=qa['context'])
        
        print(f"Context: {qa['context']}")
        print("Answer: [Would be generated with citations from training data]")
        print()
        
        # Example of what a good answer looks like:
        example_answer = """
Example answer structure:
- Direct answer to the question
- Physical mechanism explanation
- Relevant equations (if applicable)
- Citations to papers/textbooks
- Connection to related concepts
        """.strip()
        print(example_answer)
        print()
        print()

if __name__ == "__main__":
    main()
