# Release Checklist: v0.1.0 (Initial Release)

**Target Date**: April 15, 2026  
**Release Manager**: @Houchen181  
**Status**: 📋 Planning

---

## Pre-Release Tasks

### Documentation
- [x] README.md complete with installation and usage
- [x] CONTRIBUTING.md with clear guidelines
- [x] CODEOWNERS defined
- [x] ROADMAP.md with future plans
- [x] BENCHMARK_PROTOCOL.md documented
- [x] STACK_DECISIONS.md explaining tech choices
- [ ] CHANGELOG.md created (template needed)
- [ ] API reference documentation (auto-generated from docstrings)
- [ ] Tutorial: "10-minute physics expert" (step-by-step guide)

### Code Quality
- [x] All tests passing (CI green)
- [x] Test coverage > 80%
- [x] No critical bugs in issues
- [x] Python type hints added to public APIs
- [x] Docstrings complete (Google style)
- [ ] Code review completed
- [ ] Performance benchmarks run and documented

### Infrastructure
- [x] GitHub Actions CI/CD working
- [x] PyPI package ready (setup.py complete)
- [ ] Docker image built and tested
- [x] Colab notebook working
- [x] Streamlit UI example functional
- [ ] Documentation website deployed (MkDocs/ReadTheDocs)

### Community
- [x] Issue templates created
- [x] PR template created
- [x] Good first issues labeled
- [x] Contributor spotlight page ready
- [ ] GitHub Discussions enabled and seeded
- [ ] Initial announcement post drafted

---

## Release Day Tasks

### Final Checks (Morning of release)
- [ ] All CI checks passing on main
- [ ] No open critical/high severity issues
- [ ] Version number updated in all files
- [ ] CHANGELOG.md finalized
- [ ] Release notes drafted

### Create Release (10:00 AM EST)
- [ ] Create git tag: `v0.1.0`
- [ ] Push tag to GitHub
- [ ] Create GitHub Release with notes
- [ ] Publish to PyPI: `pip install condensai`
- [ ] Push Docker image (if applicable)

### Announcement (12:00 PM EST)
- [ ] Twitter/X thread with demo GIF
- [ ] LinkedIn post
- [ ] Reddit post (r/MachineLearning, r/Physics, r/LocalLLaMA)
- [ ] Hacker News "Show HN" post
- [ ] Email to physics mailing lists
- [ ] Post in Discord/Slack communities

---

## Post-Release Tasks

### Week 1
- [ ] Monitor issues and PRs daily
- [ ] Respond to all feedback within 24h
- [ ] Track download/install stats
- [ ] Collect user testimonials
- [ ] Fix critical bugs within 48h

### Week 2-4
- [ ] Write follow-up blog post with initial learnings
- [ ] Update roadmap based on feedback
- [ ] Plan v0.2.0 features
- [ ] Reach out to potential contributors
- [ ] Submit to relevant journals/conferences

---

## Success Metrics

### Target (First Month)
- [ ] 100+ GitHub stars
- [ ] 10+ forks
- [ ] 5+ contributors
- [ ] 100+ PyPI downloads
- [ ] 3+ community issues/PRs
- [ ] 1+ blog post or tutorial by external user

### Stretch Goals
- [ ] 500+ stars
- [ ] 50+ forks
- [ ] 20+ contributors
- [ ] 1000+ PyPI downloads
- [ ] Featured in newsletter or podcast

---

## Release Notes Template

```markdown
## CondensAI v0.1.0 - Initial Release

🎉 We're excited to announce the first release of CondensAI!

### What's New
- Core RAG pipeline for physics Q&A
- LoRA fine-tuning support
- CMPhysBench evaluation framework
- Streamlit UI example
- Colab-ready demo notebook

### Installation
```bash
pip install condensai
```

### Quick Start
[Link to tutorial]

### Documentation
[Link to docs]

### Contributors
Thank you to all contributors!

### What's Next
- Dense retrieval (sentence-transformers)
- Cross-encoder reranking
- Extended benchmarks
```

---

## Rollback Plan (If Critical Issues Found)

If critical issues are discovered post-release:

1. **Immediate** (< 1 hour): Acknowledge issue publicly
2. **Short-term** (< 24 hours): Release patch (v0.1.1) or yank release
3. **Communication**: Update release notes, issue statement
4. **Learning**: Document lessons learned for next release

---

*Last updated: 2026-03-18*  
*Release manager: @Houchen181*
