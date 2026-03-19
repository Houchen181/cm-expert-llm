"""
Benchmark Evaluations for cm-expert-llm.

Implements evaluation metrics for condensed matter physics LLM assessment:
- CMPhysBench-style: Domain knowledge, problem-solving, reasoning
- CMT-Benchmark-style: Concept understanding, mathematical formalism
- Grounding metrics: Faithfulness, citation accuracy, hallucination detection
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class BenchmarkType(str, Enum):
    """Types of benchmarks supported."""
    KNOWLEDGE = "knowledge"
    PROBLEM_SOLVING = "problem_solving"
    REASONING = "reasoning"
    GROUNDING = "grounding"
    MATHEMATICAL = "mathematical"


@dataclass
class BenchmarkQuestion:
    """Single benchmark question structure."""
    id: str
    question: str
    context: Optional[str] = None
    expected_answer: Optional[str] = None
    multiple_choice_options: Optional[List[str]] = None
    benchmark_type: str = BenchmarkType.KNOWLEDGE
    difficulty: str = "medium"  # easy, medium, hard
    topic: str = "general"  # e.g., superconductivity, topology, etc.
    references: Optional[List[str]] = None


@dataclass
class EvaluationResult:
    """Result of evaluating a single question."""
    question_id: str
    model_answer: str
    is_correct: bool
    confidence: float
    latency_ms: float
    grounding_score: Optional[float] = None
    reasoning_steps: Optional[List[str]] = None


@dataclass
class BenchmarkReport:
    """Aggregated benchmark report."""
    benchmark_name: str
    total_questions: int
    answered: int
    correct: int
    accuracy: float
    avg_confidence: float
    avg_latency_ms: float
    by_difficulty: Dict[str, Dict[str, float]]
    by_topic: Dict[str, Dict[str, float]]
    grounding_avg: Optional[float] = None
    hallucination_rate: Optional[float] = None


class CMPBenchmark:
    """
    Condensed Matter Physics Benchmark evaluator.
    
    Evaluates LLM performance on:
    - Domain knowledge (concepts, phenomena, materials)
    - Problem solving (calculations, derivations)
    - Reasoning (physical intuition, approximations)
    - Grounding (citation accuracy, faithfulness to sources)
    """
    
    def __init__(self, benchmark_file: Optional[Path] = None):
        """Initialize with optional custom benchmark file."""
        self.benchmark_file = benchmark_file or self._default_benchmark_path()
        self.questions: List[BenchmarkQuestion] = []
        self.results: List[EvaluationResult] = []
        self._load_benchmark()
    
    def _default_benchmark_path(self) -> Path:
        """Return default benchmark file path."""
        return Path(__file__).parent / "data" / "cmphys_bench.jsonl"
    
    def _load_benchmark(self) -> None:
        """Load benchmark questions from file."""
        if not self.benchmark_file.exists():
            self._create_default_benchmark()
            if not self.benchmark_file.exists():
                return
        
        with open(self.benchmark_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    self.questions.append(BenchmarkQuestion(**data))
    
    def _create_default_benchmark(self) -> None:
        """Create default benchmark questions."""
        default_questions = [
            BenchmarkQuestion(
                id="cm_knowledge_001",
                question="What is the physical origin of the Meissner effect in conventional superconductors?",
                expected_answer="The Meissner effect arises from the formation of Cooper pairs and the resulting diamagnetic screening currents that expel magnetic flux from the superconductor interior.",
                benchmark_type=BenchmarkType.KNOWLEDGE,
                difficulty="medium",
                topic="superconductivity"
            ),
            BenchmarkQuestion(
                id="cm_knowledge_002",
                question="Explain the difference between topological insulators and conventional band insulators.",
                expected_answer="Topological insulators have conducting surface states protected by time-reversal symmetry, while conventional insulators have no conducting states at the Fermi level.",
                benchmark_type=BenchmarkType.KNOWLEDGE,
                difficulty="medium",
                topic="topology"
            ),
            BenchmarkQuestion(
                id="cm_problem_001",
                question="Calculate the Fermi energy for a 2D electron gas with density n = 10^15 m^-2.",
                expected_answer="E_F = (ℏ²πn)/m* �?0.037 eV (for m* = 0.067m_e)",
                benchmark_type=BenchmarkType.PROBLEM_SOLVING,
                difficulty="hard",
                topic="electronic_structure"
            ),
            BenchmarkQuestion(
                id="cm_reasoning_001",
                question="Why does the specific heat of a superconductor show an exponential temperature dependence at low T?",
                expected_answer="Due to the presence of an energy gap Δ in the quasiparticle spectrum, leading to exponentially suppressed thermal excitations: C �?exp(-Δ/k_BT).",
                benchmark_type=BenchmarkType.REASONING,
                difficulty="hard",
                topic="superconductivity"
            ),
            BenchmarkQuestion(
                id="cm_math_001",
                question="Write down the BCS gap equation and explain each term.",
                expected_answer="Δ_k = -Σ_k' V_kk' (Δ_k' / 2E_k') tanh(E_k' / 2k_BT), where Δ is the gap, V is the pairing interaction, E is the quasiparticle energy.",
                benchmark_type=BenchmarkType.MATHEMATICAL,
                difficulty="hard",
                topic="superconductivity"
            ),
        ]
        
        self.benchmark_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.benchmark_file, 'w', encoding='utf-8') as f:
            for q in default_questions:
                f.write(json.dumps(asdict(q)) + '\n')
        
        self.questions = default_questions
    
    def evaluate_answer(self, question: BenchmarkQuestion, answer: str) -> EvaluationResult:
        """
        Evaluate a single answer.
        
        Args:
            question: The benchmark question
            answer: Model's answer to evaluate
        
        Returns:
            EvaluationResult with correctness and metrics
        """
        # TODO: Implement LLM-based evaluation
        # For now, use simple string matching as placeholder
        is_correct = False
        confidence = 0.0
        
        if question.expected_answer:
            # Simple keyword matching as placeholder
            expected_lower = question.expected_answer.lower()
            answer_lower = answer.lower()
            
            # Check for key terms
            key_terms = [word for word in expected_lower.split() if len(word) > 4]
            matches = sum(1 for term in key_terms if term in answer_lower)
            confidence = min(1.0, matches / max(len(key_terms), 1))
            is_correct = confidence > 0.5
        
        return EvaluationResult(
            question_id=question.id,
            model_answer=answer,
            is_correct=is_correct,
            confidence=confidence,
            latency_ms=0.0  # TODO: measure actual latency
        )
    
    def run_full_benchmark(self, model_fn, save_results: bool = True) -> BenchmarkReport:
        """
        Run complete benchmark evaluation.
        
        Args:
            model_fn: Function that takes question string and returns answer
            save_results: Whether to save results to file
        
        Returns:
            BenchmarkReport with aggregated metrics
        """
        self.results = []
        
        for question in self.questions:
            try:
                answer = model_fn(question.question, question.context)
                result = self.evaluate_answer(question, answer)
                self.results.append(result)
            except Exception as e:
                print(f"Error evaluating {question.id}: {e}")
        
        return self._generate_report(save_results)
    
    def _generate_report(self, save: bool = False) -> BenchmarkReport:
        """Generate aggregated report from results."""
        if not self.results:
            raise ValueError("No results to generate report from")
        
        correct = sum(1 for r in self.results if r.is_correct)
        total = len(self.results)
        
        # Group by difficulty
        by_difficulty = {}
        by_topic = {}
        
        for result in self.results:
            question = next((q for q in self.questions if q.id == result.question_id), None)
            if question:
                # By difficulty
                diff = question.difficulty
                if diff not in by_difficulty:
                    by_difficulty[diff] = {"correct": 0, "total": 0}
                by_difficulty[diff]["total"] += 1
                if result.is_correct:
                    by_difficulty[diff]["correct"] += 1
                
                # By topic
                topic = question.topic
                if topic not in by_topic:
                    by_topic[topic] = {"correct": 0, "total": 0}
                by_topic[topic]["total"] += 1
                if result.is_correct:
                    by_topic[topic]["correct"] += 1
        
        # Calculate accuracies
        for diff in by_difficulty:
            d = by_difficulty[diff]
            d["accuracy"] = d["correct"] / d["total"] if d["total"] > 0 else 0.0
        
        for topic in by_topic:
            t = by_topic[topic]
            t["accuracy"] = t["correct"] / t["total"] if t["total"] > 0 else 0.0
        
        avg_confidence = sum(r.confidence for r in self.results) / len(self.results)
        avg_latency = sum(r.latency_ms for r in self.results) / len(self.results)
        
        report = BenchmarkReport(
            benchmark_name="CMPhysBench",
            total_questions=total,
            answered=len(self.results),
            correct=correct,
            accuracy=correct / total if total > 0 else 0.0,
            avg_confidence=avg_confidence,
            avg_latency_ms=avg_latency,
            by_difficulty=by_difficulty,
            by_topic=by_topic,
            grounding_avg=None,
            hallucination_rate=None
        )
        
        if save:
            self._save_report(report)
        
        return report
    
    def _save_report(self, report: BenchmarkReport) -> None:
        """Save report to file."""
        report_dir = Path(__file__).parent / "results"
        report_dir.mkdir(parents=True, exist_ok=True)
        
        report_file = report_dir / f"benchmark_{Path(self.benchmark_file).stem}_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(report), f, indent=2)
        
        print(f"Benchmark report saved to: {report_file}")


def main():
    """Run benchmark evaluation."""
    import argparse
    parser = argparse.ArgumentParser(description='Run cm-expert-llm benchmark')
    parser.add_argument('--benchmark-file', type=str, help='Custom benchmark file')
    parser.add_argument('--save', action='store_true', help='Save results')
    args = parser.parse_args()
    
    benchmark = CMPBenchmark(
        benchmark_file=Path(args.benchmark_file) if args.benchmark_file else None
    )
    
    print(f"Loaded {len(benchmark.questions)} benchmark questions")
    print("To run full evaluation, provide a model function")
    
    # Print sample questions
    for i, q in enumerate(benchmark.questions[:3]):
        print(f"\n{i+1}. [{q.topic}] {q.difficulty}")
        print(f"   Q: {q.question}")
        if q.expected_answer:
            print(f"   A: {q.expected_answer[:100]}...")


if __name__ == '__main__':
    main()
