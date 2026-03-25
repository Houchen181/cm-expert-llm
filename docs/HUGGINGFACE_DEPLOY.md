# Deploy to Hugging Face Spaces

This guide shows how to deploy CondensAI as a free, public demo on Hugging Face Spaces.

## Why Hugging Face Spaces?

- **Free hosting** for public demos (CPU and GPU options)
- **Built-in audience** of 500k+ ML practitioners
- **One-click deployment** from GitHub
- **Automatic SSL** and HTTPS
- **Easy sharing** with embeddable widgets

## Quick Deploy (5 minutes)

### Step 1: Create a Hugging Face Account

1. Go to https://huggingface.co
2. Click "Sign Up" (top right)
3. Create account (GitHub login recommended)

### Step 2: Create New Space

1. Click your profile icon → "New Space"
2. Configure:
   - **Space name**: `condensai-demo` (or your choice)
   - **License**: MIT
   - **Visibility**: Public
3. Click "Create Space"

### Step 3: Choose SDK

Select **Streamlit** (we provide `examples/05_streamlit_ui.py`)

### Step 4: Connect GitHub Repository

**Option A: Direct GitHub Integration** (Recommended)

1. In your Space, click "Files" → "Add file" → "Import from GitHub"
2. Authorize Hugging Face to access your GitHub
3. Select repository: `Houchen181/cm