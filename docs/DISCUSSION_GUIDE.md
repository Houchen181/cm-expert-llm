# GitHub Discussions Guide

This guide helps seed and structure GitHub Discussions for cm-expert-llm.

## Why Discussions Matter

GitHub Discussions provide a space for:
- Questions that aren't bugs
- Feature ideas and brainstorming
- Showcasing what you built
- Community support
- Announcements

## Enabling Discussions

**For maintainers:**
1. Go to: https://github.com/Houchen181/cm-expert-llm/settings
2. Click "Discussions" in left sidebar
3. Check "Enable Discussions"
4. Configure categories (see below)

## Discussion Categories

Create these categories:

### 1. 📢 Announcements
- **Purpose**: Official project updates
- **Who can post**: Maintainers only
- **Examples**:
  - Release announcements (v0.1.0, v0.2.0)
  - Roadmap updates
  - Community highlights

### 2. 💬 General
- **Purpose**: Casual conversation
- **Who can post**: Everyone
- **Examples**:
  - Introductions
  - Off-topic physics chat
  - "What are you working on?"

### 3. �?Q&A
- **Purpose**: Ask for help
- **Who can post**: Everyone
- **Examples**:
  - "How do I install cm-expert-llm?"
  - "Error: module not found"
  - "Best practices for X?"

### 4. 💡 Ideas
- **Purpose**: Feature requests and brainstorming
- **Who can post**: Everyone
- **Examples**:
  - "Add support for X physics domain"
  - "Improve Y performance"
  - "New evaluation metric idea"

### 5. 🎉 Showcase
- **Purpose**: Share what you built
- **Who can post**: Everyone
- **Examples**:
  - "I deployed cm-expert-llm for my research group"
  - "Here's my custom physics expert"
  - "Benchmark results on my dataset"

### 6. 📚 Tutorials
- **Purpose**: Community tutorials and guides
- **Who can post**: Everyone
- **Examples**:
  - "How I used cm-expert-llm for teaching"
  - "Custom dataset preparation guide"
  - "Integration with other tools"

## Starter Discussion Posts

### Welcome Post (Pin this!)

```markdown
# Welcome to cm-expert-llm Discussions! 🦀

This is the place to:
- Ask questions about using cm-expert-llm
- Suggest new features
- Share what you've built
- Connect with other physics researchers

## Getting Started
- 📖 [Read the docs](docs/)
- 🚀 [Try the Colab demo](examples/03_demo.ipynb)
- 📝 [Check out the roadmap](ROADMAP.md)
- 🤝 [See how to contribute](CONTRIBUTING.md)

## Need Help?
- For bugs: [Open an issue](https://github.com/Houchen181/cm-expert-llm/issues/new)
- For questions: Start a [Q&A discussion](link)
- For ideas: Post in [Ideas category](link)

Introduce yourself below! 👇
```

### First Question Template

```markdown
# [Q&A] How to get started with cm-expert-llm?

**Question**: I'm new to cm-expert-llm and want to deploy my own physics expert. Where should I start?

**Context**: 
- My background: [e.g., PhD student in condensed matter physics]
- My goal: [e.g., Build a Q&A bot for my research group's papers]
- What I've tried: [e.g., Read README, ran the Colab demo]

**Question**: What's the best path forward for my use case?
```

## Moderation Guidelines

### For Maintainers
- **Be welcoming**: First impressions matter
- **Be patient**: Not everyone knows git/ML
- **Be encouraging**: Thank people for contributions
- **Be responsive**: Aim for <48h response time

### For Everyone
- **Be kind**: We're all here to help
- **Be constructive**: Critique ideas, not people
- **Be specific**: Provide context and examples
- **Search first**: Your question may already be answered

## Discussion �?Issue Conversion

When a discussion reveals a bug or clear feature request:

1. **Acknowledge**: "Thanks for reporting this!"
2. **Convert**: Use "Convert to issue" button (GitHub feature)
3. **Link**: Add link to new issue in discussion
4. **Follow up**: Keep discussion updated on progress

## Metrics to Track

- **Total discussions**: Target 50+ in first month
- **Active participants**: Target 20+ unique users
- **Resolution rate**: % of Q&A marked as answered
- **Response time**: Average time to first reply
- **Conversion rate**: Discussions �?Issues �?PRs

## Promotion

Announce Discussions in:
- README.md (add badge)
- Issue templates
- PR templates
- Social media posts
- Release notes

---

*Last updated: 2026-03-18*

*This guide evolves with the community. Suggestions welcome!*
