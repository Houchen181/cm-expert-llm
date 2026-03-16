"""
Run benchmark evaluations for CondensAI.
Supports:
- CMPhysBench: Condensed matter physics problems
- CMT-Benchmark: Theory understanding
- Grounding metrics: Faithfulness and citation accuracy
"""

import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

from .benchmarks import CMPBenchmark, BenchmarkQuestion
from .grounding import GroundingEvaluator, GroundingEvaluation


def load_model_answer_function(model_type: str = "placeholder"):
    """
    Load or create a function that generates answers.
    
    In production, this would load a trained model.
    For now, returns a placeholder function.
    """
    def answer_fn(question: str, context: Optional[str] = None) -> str:
        """Placeholder answer function."""
        return f"[Placeholder answer for: {question[:50]}...]"
    
    return answer_fn


def run_cmphys_bench(benchmark_path: Optional[Path] = None, 
                     save_results: bool = True) -> Dict[str, Any]:
    """
    Run CMPhysBench evaluation.
    
    Args:
        benchmark_path: Path to benchmark file (uses default if None)
        save_results: Whether to save results to file
        
    Returns:
        Dictionary with benchmark results
    """
    print("Running CMPhysBench evaluation...")
    
    benchmark = CMPBenchmark(benchmark_path)
    
    if not benchmark.questions:
        print("No benchmark questions loaded!")
        return {"error": "No questions"}
    
    print(f"Loaded {len(benchmark.questions)} benchmark questions")
    
    # Print sample questions
    print("\nSample questions:")
    for i, q in enumerate(benchmark.questions[:3]):
        print(f"  {i+1}. [{q.topic}] {q.difficulty}: {q.question[:80]}...")
    
    # Run evaluation with placeholder model
    model_fn = load_model_answer_function()
    
    print("\nEvaluating...")
    report = benchmark.run_full_benchmark(model_fn, save_results=save_results)
    
    # Print results
    print(f"\n{'='*60}")
    print(f"Benchmark: {report.benchmark_name}")
    print(f"Total Questions: {report.total_questions}")
    print(f"Accuracy: {report.accuracy:.2%}")
    print(f"Avg Confidence: {report.avg_confidence:.2%}")
    
    print("\nBy Difficulty:")
    for diff, stats in report.by_difficulty.items():
        print(f"  {diff}: {stats.get('accuracy', 0):.2%} ({stats.get('correct', 0)}/{stats.get('total', 0)})")
    
    print("\nBy Topic:")
    for topic, stats in report.by_topic.items():
        print(f"  {topic}: {stats.get('accuracy', 0):.2%} ({stats.get('correct', 0)}/{stats.get('total', 0)})")
    
    return {
        "benchmark_name": report.benchmark_name,
        "total_questions": report.total_questions,
        "accuracy": report.accuracy,
        "by_difficulty": report.by_difficulty,
        "by_topic": report.by_topic
    }


def run_grounding_eval(corpus_path: Optional[Path] = None,
                       responses_file: Optional[Path] = None,
                       save_results: bool = True) -> Dict[str, Any]:
    """
    Run grounding evaluation on responses.
    
    Args:
        corpus_path: Path to JSONL corpus for grounding sources
        responses_file: Path to JSON file with responses to evaluate
        save_results: Whether to save results
        
    Returns:
        Dictionary with grounding evaluation results
    """
    print("Running grounding evaluation...")
    
    evaluator = GroundingEvaluator()
    
    # Load corpus if provided
    if corpus_path and corpus_path.exists():
        count = evaluator.load_sources_from_corpus(corpus_path)
        print(f"Loaded {count} source documents")
    else:
        print("No corpus provided, skipping source grounding")
    
    # Load responses if provided
    responses = {}
    if responses_file and responses_file.exists():
        with open(responses_file, 'r') as f:
            responses = json.load(f)
        print(f"Loaded {len(responses)} responses to evaluate")
    else:
        # Use sample responses
        responses = {
            "resp_001": "The Meissner effect is the expulsion of magnetic flux from a superconductor.",
            "resp_002": "Topological insulators have conducting surface states protected by time-reversal symmetry.",
            "resp_003": "The BCS gap equation is Δ = V * Σ(k') [Δ / 2E] tanh(E/2kT) [1, 2]"
        }
        print("Using sample responses")
    
    # Evaluate each response
    results = {}
    for resp_id, text in responses.items():
        evaluation = evaluator.evaluate_response(text, resp_id)
        results[resp_id] = {
            "text": text,
            "grounding_ratio": evaluation.grounding_ratio,
            "hallucinated_claims": evaluation.hallucinated_claims,
            "citation_accuracy": evaluation.citation_accuracy,
            "overall_score": evaluation.overall_score
        }
        
        print(f"\n{resp_id}:")
        print(f"  Grounding: {evaluation.grounding_ratio:.2%}")
        print(f"  Overall Score: {evaluation.overall_score:.2%}")
    
    # Generate report
    report = evaluator.generate_report()
    
    if save_results:
        output_path = Path("results/grounding_eval.json")
        output_path.parent.mkdir(exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\nGrounding report saved to: {output_path}")
    
    return report


def main():
    """Main evaluation runner."""
    parser = argparse.ArgumentParser(description='Run CondensAI evaluations')
    parser.add_argument('--benchmark', action='store_true', 
                       help='Run CMPhysBench evaluation')
    parser.add_argument('--grounding', action='store_true',
                       help='Run grounding evaluation')
    parser.add_argument('--all', action='store_true',
                       help='Run all evaluations')
    parser.add_argument('--benchmark-file', type=str,
                       help='Custom benchmark file path')
    parser.add_argument('--corpus', type=str, default='./data/processed/sft.jsonl',
                       help='Corpus file for grounding')
    parser.add_argument('--output', type=str, default='./results',
                       help='Output directory')
    
    args = parser.parse_args()
    
    # Default to all if nothing specified
    run_benchmark = args.benchmark or args.all or (not args.grounding)
    run_grounding = args.grounding or args.all or (not args.benchmark)
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "evaluations": {}
    }
    
    if run_benchmark:
        benchmark_results = run_cmphys_bench(
            benchmark_path=Path(args.benchmark_file) if args.benchmark_file else None
        )
        results["evaluations"]["cmphys_bench"] = benchmark_results
    
    if run_grounding:
        grounding_results = run_grounding_eval(
            corpus_path=Path(args.corpus),
        )
        results["evaluations"]["grounding"] = grounding_results
    
    # Save combined results
    output_path = Path(args.output) / "evaluation_results.json"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Evaluation complete! Results saved to: {output_path}")
    
    return results


if __name__ == '__main__':
    main()
