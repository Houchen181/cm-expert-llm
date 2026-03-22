# GitHub Discussions Setup Guide

This guide helps you set up GitHub Discussions for the cm-expert-llm community.

## 🎯 Why Enable Discussions?

GitHub Discussions is crucial for community building:
- **Q&A**: Separate questions from bugs (reduces issue clutter)
- **Ideas**: Collect feature requests before they become issues
- **Showcase**: Let users share their physics models and results
- **Announcements**: Official project updates
- **Community**: Build a space for condensed matter physicists using LLMs

## 📋 Step-by-Step Setup

### Step 1: Enable Discussions

1. Go to: https://github.com/Houchen181/cm-expert-llm/settings
2. Scroll to **"Features"** section
3. Check the box for **"Discussions"** ✓
4. Click **"Set up in Discussions"**

### Step 2: Configure Categories

Create these categories (in order):

#### 1. 📢 Announcements
- **Type**: Announcement (pinned, locked threads)
- **Purpose**: Official project updates, release notes
- **Who can post**: Maintainers only

#### 2. ❓ Q&A
- **Type**: Q&A (voting enabled)
- **Purpose**: Ask and answer questions
- **Description**: "Stuck on something? Ask here! Search first to see if your question was already answered."
- **Who can post**: Everyone

#### 3. 💡 Ideas
- **Type**: Idea (voting enabled)
- **Purpose**: Feature requests and suggestions
- **Description**: "Suggest new features, improvements, or physics content. Upvote ideas you'd like to see!"
- **Who can post**: Everyone

#### 4. 🎉 Showcase
- **Type**: Discussion (voting enabled)
- **Purpose**: Share your physics models, results, tutorials
- **Description**: "Show off what you built with cm-expert-llm! Share your custom models, teaching materials, or research results."
- **Who can post**: Everyone

#### 5. 📚 Tutorials
- **Type**: Discussion (voting enabled)
- **Purpose**: Community tutorials, guides, tips
- **Description**: "Share and find tutorials, tips, and best practices for using cm-expert-llm."
- **Who can post**: Everyone

### Step 3: Seed Initial Discussions

Create these starter discussions:

#### Announcement Category:
1. **"Welcome to cm-expert-llm Discussions!"**
   - Welcome message
   - How to use each category
   - Code of conduct reminder

2. **"v0.1.0 Release Notes"** (when ready)
   - Link to release
   - Key features
   - Upgrade guide

#### Q&A Category:
1. **"FAQ: Common Questions"** (pinned)
   - Installation issues
   - Training questions
   - Data format questions
   - Link to docs

#### Ideas Category:
1. **"Feature Request Template"** (pinned)
   - How to submit good feature requests
   - What information to include

2. **"Physics Content Requests"** (pinned)
   - What subfields need more coverage
   - How to contribute papers/notes

#### Showcase Category:
1. **"Share Your Model!"**
   - Encourage users to post their custom models
   - Template: What physics, what data, what results

2. **"Teaching with cm-expert-llm"**
   - Educators share how they use it in courses
   - Student projects

### Step 4: Configure Settings

In **Discussion Settings**:
- ✅ Enable voting on ideas and showcase
- ✅ Enable markdown formatting
- ✅ Enable code blocks
- ✅ Allow users to edit their posts
- ✅ Notify maintainers of new discussions
- ❌ Disable auto-lock (keep conversations open)

### Step 5: Add Badges to README

Once set up, add to README.md:
```markdown
[![Discussions](https://img.shields.io/badge/discussions-join-blue)](https://github.com/Houchen181/cm-expert-llm/discussions)
```

## 🎯 Discussion Templates

### Welcome Message Template
```markdown
# Welcome to cm-expert-llm Discussions! 👋

This is the place to:
- ❓ Ask questions about the project
- 💡 Suggest new features
- 🎉 Share your physics models
- 📚 Find and share tutorials

## Quick Links
- [Documentation](docs/)
- [Examples](examples/)
- [Contributing Guide](CONTRIBUTING.md)

## Categories
- **Q&A**: Get help with installation, usage, or physics content
- **Ideas**: Suggest features or improvements
- **Showcase**: Share what you built!
- **Tutorials**: Learn from others' experiences

Be respectful and helpful. This is a community space for condensed matter physicists and ML enthusiasts!

---
*Project maintainers monitor all categories and will respond to questions and ideas.*
```

### FAQ Template
```markdown
# FAQ: Frequently Asked Questions

## Installation
**Q: How do I install cm-expert-llm?**
A: See [INSTALL.md](docs/INSTALL.md) for step-by-step instructions.

**Q: Do I need a GPU?**
A: For training, yes. For inference with small models, CPU works but is slower.

## Training
**Q: How much data do I need?**
A: Start with 10-20 papers or ~100k tokens. More is better!

**Q: Can I use my own papers?**
A: Absolutely! That's the whole point. See [data/raw/README.md](data/raw/README.md).

## Physics Content
**Q: What subfields are covered?**
A: Currently: superconductivity, topology, correlated electrons. More coming!

**Q: Can I contribute my lecture notes?**
A: Yes! See [CONTRIBUTING.md](CONTRIBUTING.md).

---
Have more questions? Start a new discussion in the Q&A category!
```

## 📊 Success Metrics

Track these to measure community health:
- **Discussions per week**: Target 5+
- **Response time**: < 24 hours for questions
- **Active participants**: Target 10+ unique users/month
- **Solved Q&A**: > 80% resolution rate
- **Showcase posts**: Target 2+ per month

## 🎯 Best Practices

### For Maintainers:
- **Respond quickly** to questions (< 24h ideal)
- **Upvote good ideas** and comment constructively
- **Pin important discussions**
- **Lock off-topic or resolved threads** (politely)
- **Thank contributors** publicly

### For Users:
- **Search first** before posting
- **Be specific** in questions
- **Upvote** useful ideas
- **Share results** in showcase
- **Help others** in Q&A

## 🚀 After Setup

Once discussions are enabled:
1. Add discussion badge to README
2. Link to discussions in CONTRIBUTING.md
3. Mention in release notes
4. Encourage users to post questions there (not issues)
5. Reference good discussions in docs

---

**Questions about this guide?** Start a discussion! 😊

*Last updated: March 22, 2026*
