# Repository Rename Proposal

## Current Name
- **Current:** `cm-expert-llm`
- **URL:** https://github.com/Houchen181/cm-expert-llm

## Problem
The current name `cm-expert-llm` is functional but not memorable or brandable. To reach 1k stars, we need a name that:
- Is catchy and easy to remember
- Clearly indicates the domain (condensed matter physics)
- Suggests AI/LLM capability
- Is searchable and unique on GitHub

## Proposed Shortlist (Top 5)

| Rank | Name | Pros | Cons | Availability Check |
|------|------|------|------|-------------------|
| 1 | **CondensAI** | Short, memorable, combines "condensed" + "AI", unique | May be confused with general condensed matter AI (not just LLM) | ✅ Need to verify |
| 2 | **MatterLLM** | Direct, clear, indicates matter physics + LLM | Slightly generic | ✅ Need to verify |
| 3 | **PhysicLLM** | Physics + LLM, clear domain | Less specific to condensed matter | ✅ Need to verify |
| 4 | **SolidStateAI** | Refers to solid-state physics (subset of CM) | May be too narrow (excludes soft matter, etc.) | ✅ Need to verify |
| 5 | **QuarkLLM** | Short, physics-related, memorable | Quarks are particle physics, not condensed matter (misleading) | ✅ Need to verify |

## Recommendation
**Top Pick: CondensAI**
- Strongest brand potential
- Clear condensed matter connection
- AI suffix makes it modern
- Easy to spell and search

**Runner-up: MatterLLM**
- More generic but clearer about LLM focus
- Good if CondensAI is taken

## Migration Checklist

Once a new name is selected and verified available:

### Pre-Migration
- [ ] Verify new name availability on GitHub
- [ ] Create backup of current repository (export zip)
- [ ] Notify any existing contributors/stargazers (if applicable)

### GitHub Actions
- [ ] Rename repository on GitHub (Settings → Rename)
- [ ] Update repository description if needed
- [ ] Verify GitHub Pages/deployments still work

### Local Updates
- [ ] Update git remote URL:
  ```bash
  git remote set-url origin https://github.com/Houchen181/<NEW-NAME>.git
  ```
- [ ] Update all internal references:
  - [ ] README.md (badges, links, project name)
  - [ ] All documentation files (`docs/*.md`)
  - [ ] Configuration files (`configs/*.yaml`)
  - [ ] Python package metadata (`pyproject.toml`, `setup.py`)
  - [ ] Import paths if package name changes
  - [ ] Example notebooks (`examples/*.ipynb`)
  - [ ] CI/CD workflows (`.github/workflows/*.yml`)

### Post-Migration
- [ ] Test all links in README
- [ ] Verify badges point to correct repo
- [ ] Update any external references (papers, tutorials, docs)
- [ ] Add redirect note in old README if creating new repo instead of renaming
- [ ] Update HEARTBEAT.md with new name

### Communication
- [ ] Update project description in all social/docs
- [ ] If renaming, GitHub auto-redirects old URLs (but update anyway)
- [ ] Announce rename in changelog/release notes

## Decision Needed
**Action Required from User:**
1. Select preferred name from shortlist (or propose alternative)
2. Verify availability on GitHub
3. Confirm rename approach (rename existing vs. create new + migrate)

Once confirmed, I will execute the full migration checklist.

---
*Created: 2026-03-15 19:50 EDT*
*Status: Awaiting user decision on name selection*
