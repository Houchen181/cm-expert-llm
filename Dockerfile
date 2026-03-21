# cm-expert-llm Docker Image
# One-line deployment for domain-expert LLM in condensed matter physics
# 
# Usage:
#   docker build -t cm-expert-llm .
#   docker run -p 8000:8000 cm-expert-llm

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Install the package
RUN pip install -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DRY_RUN=0

# Expose API port
EXPOSE 8000

# Default command: run the API server
CMD ["python", "-m", "uvicorn", "src.cm_expert.serve.api:app", "--host", "0.0.0.0", "--port", "8000"]
