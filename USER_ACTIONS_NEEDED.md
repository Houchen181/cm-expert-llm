# User Actions Required

This file lists actions that require your direct involvement (GitHub authentication, API keys, etc.).

## 1. Create GitHub Repository (URGENT - Blocker)

**Status:** ⏳ Pending user action

**What needs to be done:**
Create a new public GitHub repository named `cm-expert-llm` and push the local scaffold.

**Option A: Using GitHub CLI (Recommended if `gh` is installed)**
```bash
# Navigate to project directory
cd C:\Users\xu\.openclaw\workspace\llm_physics_project

# Create repository and push
gh repo create cm-expert-llm --public --description "Domain-expert LLM for condensed matter physics" --source=. --push
```

**Option B: Manual GitHub Web Interface**
1. Go to https://github.com/new
2. Repository name: `cm-expert-llm`
3. Description: "Domain-expert LLM for condensed matter physics"
4. Visibility: Public
5. Do NOT initialize with README (we already have one)
6. Click "Create repository"
7. Then run these commands in the project directory:
```bash
cd C:\Users\xu\.openclaw\workspace\llm_physics_project
git init -b main
git remote add origin https://github.com/YOUR_USERNAME/cm-expert-llm.git
git add .
git commit -m "Initial scaffold for CM-Expert-LLM project"
git push -u origin main
```

**Option C: GitHub Desktop**
1. Use "Add Local Repository" in GitHub Desktop
2. Point to: `C:\Users\xu\.openclaw\workspace\llm_physics_project`
3. Publish to GitHub as `cm-expert-llm`

---

## 2. API Keys and Configuration (Optional - For Enhanced Features)

### Brave Search API Key (for web_search tool)
- Get key from: https://brave.com/search/api/
- Set via: `openclaw configure --section web`
- Alternative: Project uses Tavily fallback (already working)

### Hugging Face Token (for model downloads/training)
- Get token from: https://huggingface.co/settings/tokens
- Add to `.env` file in project root:
```
HUGGINGFACE_TOKEN=your_token_here
```

---

## 3. Next Steps After Repo Creation

Once the repository is created and pushed:
1. ✅ Verify CI workflow runs on GitHub Actions
2. ✅ Add repository link to README.md
3. ✅ Create initial release tag (v0.1.0-scaffold)
4. 🔄 Begin implementing data ingestion pipeline
5. 🔄 Set up training infrastructure

---

## Progress Tracking

- [x] Local scaffold created
- [x] Core configuration files added
- [x] Data pipeline implemented (pipeline.py)
- [x] Standard open-source files added (CONTRIBUTING, CODE_OF_CONDUCT)
- [ ] GitHub repository created
- [ ] Initial commit pushed
- [ ] CI workflow verified
- [ ] First training run completed

---

**Last Updated:** 2026-03-13 13:08 EDT  
**Heartbeat Status:** RESUMED
