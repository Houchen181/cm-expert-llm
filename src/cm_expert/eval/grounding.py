"""
Grounding and Faithfulness Evaluation.

Evaluates whether LLM responses are properly grounded in provided sources:
- Citation accuracy
- Hallucination detection
- Faithfulness to source material
- Attribution quality
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum


class GroundingIssue(str, Enum):
    """Types of grounding issues."""
    HALLUCINATION = "hallucination"
    MISATTRIBUTION = "misattribution"
    OUT_OF_CONTEXT = "out_of_context"
    CONTRADICTION = "contradiction"
    UNSUPPORTED_CLAIM = "unsupported_claim"


@dataclass
class SourceDocument:
    """A source document for grounding evaluation."""
    id: str
    content: str
    metadata: Dict[str, Any]
    uri: Optional[str] = None


@dataclass
class Claim:
    """A claim extracted from model output."""
    text: str
    start_pos: int
    end_pos: int
    confidence: float
    category: str  # factual, inferential, opinion


@dataclass
class GroundingEvaluation:
    """Evaluation of grounding for a single response."""
    response_id: str
    total_claims: int
    grounded_claims: int
    hallucinated_claims: int
    grounding_ratio: float
    issues: List[Dict[str, Any]]
    citation_accuracy: float
    overall_score: float


class GroundingEvaluator:
    """
    Evaluates grounding and faithfulness of LLM responses.
    
    Checks:
    - Whether claims are supported by source documents
    - Citation accuracy
    - Detection of hallucinated content
    - Contextual appropriateness
    """
    
    def __init__(self):
        self.sources: Dict[str, SourceDocument] = {}
        self.evaluation_cache: Dict[str, GroundingEvaluation] = {}
    
    def add_source(self, source: SourceDocument) -> None:
        """Add a source document for grounding checks."""
        self.sources[source.id] = source
    
    def load_sources_from_corpus(self, corpus_file: Path) -> int:
        """
        Load sources from JSONL corpus file.
        
        Returns:
            Number of sources loaded
        """
        count = 0
        with open(corpus_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    source = SourceDocument(
                        id=data.get('id', f"doc_{count}"),
                        content=data.get('text', ''),
                        metadata=data.get('metadata', {}),
                        uri=data.get('metadata', {}).get('source_file')
                    )
                    self.add_source(source)
                    count += 1
        return count
    
    def extract_claims(self, text: str) -> List[Claim]:
        """
        Extract factual claims from text.
        
        Uses heuristics to identify claims that need grounding:
        - Statements with specific facts
        - References to sources/citations
        - Technical assertions
        """
        claims = []
        
        # Simple sentence-based claim extraction
        # TODO: Upgrade to NLP-based claim extraction
        sentences = re.split(r'[.!?]+', text)
        
        pos = 0
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 20:
                pos += len(sentence) + 1
                continue
            
            # Identify factual claims (simple heuristics)
            is_claim = any([
                re.search(r'\b(is|are|was|were|has|have|shows|demonstrates|indicates)\b', sentence.lower()),
                re.search(r'\b(according to|based on|as shown|evidence suggests)\b', sentence.lower()),
                re.search(r'\[\d+\]', sentence),  # Citations
            ])
            
            if is_claim or len(sentence) > 50:
                claims.append(Claim(
                    text=sentence,
                    start_pos=pos,
                    end_pos=pos + len(sentence),
                    confidence=0.8 if is_claim else 0.5,
                    category="factual" if is_claim else "inferential"
                ))
            
            pos += len(sentence) + 1
        
        return claims
    
    def check_claim_grounding(self, claim: Claim, sources: Optional[List[str]] = None) -> Tuple[bool, Optional[str], Optional[GroundingIssue]]:
        """
        Check if a claim is grounded in sources.
        
        Args:
            claim: The claim to check
            sources: Optional list of source IDs to check against
        
        Returns:
            Tuple of (is_grounded, supporting_source_id, issue_type)
        """
        claim_text = claim.text.lower()
        
        # If specific sources provided, check only those
        sources_to_check = sources or list(self.sources.keys())
        
        for source_id in sources_to_check:
            if source_id not in self.sources:
                continue
            
            source = self.sources[source_id]
            source_text = source.content.lower()
            
            # Check for claim in source
            if claim_text in source_text:
                return (True, source_id, None)
            
            # Check for partial match (keywords)
            claim_words = set(claim_text.split())
            source_words = set(source_text.split())
            overlap = claim_words & source_words
            overlap_ratio = len(overlap) / max(len(claim_words), 1)
            
            if overlap_ratio > 0.6:
                return (True, source_id, None)
        
        # No grounding found
        return (False, None, GroundingIssue.UNSUPPORTED_CLAIM)
    
    def extract_citations(self, text: str) -> List[str]:
        """Extract citation markers from text."""
        citations = []
        
        # Match [1], [2,3], [1-5], etc.
        matches = re.findall(r'\[(\d+(?:[-,]\d+)*)\]', text)
        for match in matches:
            # Parse ranges
            for part in match.split(','):
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    citations.extend(range(start, end + 1))
                else:
                    citations.append(int(part))
        
        return sorted(set(citations))
    
    def evaluate_response(self, response: str, response_id: str = "response_001") -> GroundingEvaluation:
        """
        Evaluate grounding of a complete response.
        
        Args:
            response: The model response to evaluate
            response_id: Unique identifier for this response
        
        Returns:
            GroundingEvaluation with metrics
        """
        # Extract claims
        claims = self.extract_claims(response)
        total_claims = len(claims)
        
        if total_claims == 0:
            return GroundingEvaluation(
                response_id=response_id,
                total_claims=0,
                grounded_claims=0,
                hallucinated_claims=0,
                grounding_ratio=1.0,
                issues=[],
                citation_accuracy=1.0,
                overall_score=1.0
            )
        
        # Check each claim
        grounded_count = 0
        hallucinated_count = 0
        issues = []
        
        for claim in claims:
            is_grounded, source_id, issue_type = self.check_claim_grounding(claim)
            
            if is_grounded:
                grounded_count += 1
            else:
                hallucinated_count += 1
                if issue_type:
                    issues.append({
                        "type": issue_type,
                        "claim": claim.text,
                        "position": claim.start_pos
                    })
        
        # Check citation accuracy
        citations = self.extract_citations(response)
        citation_accuracy = 1.0
        if citations:
            valid_citations = sum(1 for c in citations if f"doc_{c-1}" in self.sources or str(c) in self.sources)
            citation_accuracy = valid_citations / len(citations)
        
        # Calculate metrics
        grounding_ratio = grounded_count / total_claims if total_claims > 0 else 1.0
        hallucination_rate = hallucinated_count / total_claims if total_claims > 0 else 0.0
        
        # Overall score (weighted combination)
        overall_score = (
            0.5 * grounding_ratio +
            0.3 * citation_accuracy +
            0.2 * (1 - hallucination_rate)
        )
        
        evaluation = GroundingEvaluation(
            response_id=response_id,
            total_claims=total_claims,
            grounded_claims=grounded_count,
            hallucinated_claims=hallucinated_count,
            grounding_ratio=grounding_ratio,
            issues=issues,
            citation_accuracy=citation_accuracy,
            overall_score=overall_score
        )
        
        self.evaluation_cache[response_id] = evaluation
        return evaluation
    
    def batch_evaluate(self, responses: Dict[str, str]) -> Dict[str, GroundingEvaluation]:
        """
        Evaluate multiple responses.
        
        Args:
            responses: Dict mapping response_id to response text
        
        Returns:
            Dict of evaluations
        """
        return {
            resp_id: self.evaluate_response(text, resp_id)
            for resp_id, text in responses.items()
        }
    
    def generate_report(self, save_path: Optional[Path] = None) -> Dict[str, Any]:
        """
        Generate aggregated grounding report.
        
        Args:
            save_path: Optional path to save report
        
        Returns:
            Report dictionary
        """
        if not self.evaluation_cache:
            return {"error": "No evaluations to report"}
        
        total_claims = sum(e.total_claims for e in self.evaluation_cache.values())
        grounded_claims = sum(e.grounded_claims for e in self.evaluation_cache.values())
        hallucinated_claims = sum(e.hallucinated_claims for e in self.evaluation_cache.values())
        
        avg_citation_accuracy = sum(e.citation_accuracy for e in self.evaluation_cache.values()) / len(self.evaluation_cache)
        avg_overall_score = sum(e.overall_score for e in self.evaluation_cache.values()) / len(self.evaluation_cache)
        
        all_issues = []
        for e in self.evaluation_cache.values():
            all_issues.extend(e.issues)
        
        issue_counts = {}
        for issue in all_issues:
            issue_type = issue.get("type", "unknown")
            issue_counts[issue_type] = issue_counts.get(issue_type, 0) + 1
        
        report = {
            "summary": {
                "total_responses": len(self.evaluation_cache),
                "total_claims": total_claims,
                "grounded_claims": grounded_claims,
                "hallucinated_claims": hallucinated_claims,
                "grounding_ratio": grounded_claims / total_claims if total_claims > 0 else 1.0,
                "hallucination_rate": hallucinated_claims / total_claims if total_claims > 0 else 0.0,
                "avg_citation_accuracy": avg_citation_accuracy,
                "avg_overall_score": avg_overall_score,
                "sources_used": len(self.sources)
            },
            "issue_breakdown": issue_counts,
            "evaluations": {
                resp_id: asdict(eval) for resp_id, eval in self.evaluation_cache.items()
            }
        }
        
        if save_path:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
            print(f"Grounding report saved to: {save_path}")
        
        return report


def main():
    """Test grounding evaluation."""
    import argparse
    parser = argparse.ArgumentParser(description='Evaluate grounding of responses')
    parser.add_argument('--corpus', type=str, help='JSONL corpus file')
    parser.add_argument('--response', type=str, help='Response text to evaluate')
    parser.add_argument('--output', type=str, help='Output report path')
    args = parser.parse_args()
    
    evaluator = GroundingEvaluator()
    
    if args.corpus:
        count = evaluator.load_sources_from_corpus(Path(args.corpus))
        print(f"Loaded {count} source documents")
    
    if args.response:
        evaluation = evaluator.evaluate_response(args.response)
        print(f"Grounding ratio: {evaluation.grounding_ratio:.2%}")
        print(f"Hallucinated claims: {evaluation.hallucinated_claims}/{evaluation.total_claims}")
        print(f"Citation accuracy: {evaluation.citation_accuracy:.2%}")
        print(f"Overall score: {evaluation.overall_score:.2%}")
        
        if evaluation.issues:
            print("\nIssues found:")
            for issue in evaluation.issues:
                print(f"  - {issue['type']}: {issue['claim'][:80]}...")
    
    if args.output:
        evaluator.generate_report(Path(args.output))


if __name__ == '__main__':
    main()
