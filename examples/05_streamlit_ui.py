#!/usr/bin/env python3
"""
Streamlit UI for cm-expert-llm - Physics Expert LLM Interface

A simple, user-friendly interface for querying your cm-expert-llm physics expert.
Perfect for non-technical users who want to interact with the model without coding.

## Usage

```bash
# Install streamlit if not already installed
pip install streamlit

# Run the UI
streamlit run examples/05_streamlit_ui.py

# Or run with:
python examples/05_streamlit_ui.py
```

## Features

- Simple chat interface for physics Q&A
- Citation display with links to sources
- Confidence scores for answers
- Conversation history
- Easy model switching

"""

import streamlit as st
import requests
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="cm-expert-llm - Physics Expert",
    page_icon="🦀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2ecc71;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .answer-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3498db;
        margin: 1rem 0;
    }
    .citation-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.3rem;
        margin-top: 1rem;
        font-size: 0.9rem;
    }
    .confidence-high { color: #27ae60; font-weight: bold; }
    .confidence-med { color: #f39c12; font-weight: bold; }
    .confidence-low { color: #e74c3c; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🦀 cm-expert-llm</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Domain-Expert LLM for Condensed Matter Physics</div>', unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API endpoint
    api_url = st.text_input(
        "API URL",
        value="http://localhost:8000",
        help="Your cm-expert-llm API server URL"
    )
    
    # Model selection
    model_choice = st.selectbox(
        "Model",
        ["cm-expert-v1", "cm-expert-lite", "custom"],
        help="Select which model to query"
    )
    
    # Max tokens
    max_tokens = st.slider(
        "Max Tokens",
        min_value=256,
        max_value=2048,
        value=512,
        step=256
    )
    
    # Temperature
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Lower = more deterministic, Higher = more creative"
    )
    
    st.divider()
    
    # Info box
    st.info("""
    **Tips:**
    - Ask specific physics questions
    - Request citations for verification
    - Check confidence scores
    - Use for study/research help
    """)
    
    st.divider()
    
    # Clear history button
    if st.button("🗑�?Clear History"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "citations" in message and message["citations"]:
            with st.expander("📚 Citations"):
                for citation in message["citations"]:
                    st.markdown(f"- {citation}")

# Chat input
if prompt := st.chat_input("Ask a physics question..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🤔 Thinking...")
        
        try:
            # Query the API
            response = requests.post(
                f"{api_url}/query",
                json={
                    "question": prompt,
                    "model": model_choice,
                    "max_tokens": max_tokens,
                    "temperature": temperature
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                answer = result.get("answer", "No answer provided.")
                citations = result.get("citations", [])
                confidence = result.get("confidence", 0.0)
                
                # Display answer
                message_placeholder.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
                
                # Display confidence
                if confidence > 0.8:
                    conf_class = "confidence-high"
                    conf_text = f"High confidence ({confidence:.1%})"
                elif confidence > 0.5:
                    conf_class = "confidence-med"
                    conf_text = f"Medium confidence ({confidence:.1%})"
                else:
                    conf_class = "confidence-low"
                    conf_text = f"Low confidence ({confidence:.1%})"
                
                st.markdown(f'<span class="{conf_class}">{conf_text}</span>', unsafe_allow_html=True)
                
                # Display citations
                if citations:
                    with st.expander("📚 Citations"):
                        for citation in citations:
                            st.markdown(f"- {citation}")
                
                # Add to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "citations": citations
                })
            else:
                error_msg = f"�?Error: API returned status {response.status_code}"
                message_placeholder.markdown(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
                
        except requests.exceptions.ConnectionError:
            error_msg = "�?Cannot connect to API server. Make sure it's running at: `python scripts/serve_api.py`"
            message_placeholder.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
        except Exception as e:
            error_msg = f"�?Error: {str(e)}"
            message_placeholder.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #7f8c8d; font-size: 0.9rem;">
  <p>Powered by <a href="https://github.com/Houchen181/cm-expert-llm">cm-expert-llm</a> | 
     Specialized in condensed matter physics</p>
</div>
""", unsafe_allow_html=True)
