## Description
Briefly describe the changes in this PR.

## Related Issue
Fixes #(issue_number) or Closes #(issue_number)

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Physics content addition (papers, textbooks, datasets)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Physics Content Checklist** (if applicable)
- [ ] All physics content is from primary sources (papers, textbooks, not AI summaries)
- [ ] Proper citations included
- [ ] Content verified for accuracy
- [ ] Format matches `data/raw/` structure

## Testing
- [ ] Tests pass: `python -m pytest tests/`
- [ ] For training changes: verified with `DRY_RUN=1` first
- [ ] For new physics content: verified format with `scripts/build_corpus.py`

## Documentation
- [ ] Updated README.md if needed
- [ ] Added docstrings to new functions/classes
- [ ] Updated examples if applicable

## Additional Notes
Any additional context for reviewers.
