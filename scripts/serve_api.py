#!/usr/bin/env python3
"""
Serve the CM Expert LLM API.

Usage:
    python scripts/serve_api.py --config configs/serve.default.yaml

Or with uvicorn directly:
    uvicorn cmp_expert.serve.api:app --host 0.0.0.0 --port 8080 --reload
"""

import argparse
import yaml
from pathlib import Path
import sys

# Add src to path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))


def load_config(config_path: str) -> dict:
    """Load YAML configuration."""
    path = Path(config_path)
    if not path.exists():
        print(f"Config not found: {config_path}, using defaults")
        return {
            'host': '0.0.0.0',
            'port': 8080,
            'reload': False,
            'workers': 1
        }
    
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description='Serve CM Expert LLM API')
    parser.add_argument('--config', type=str, default='configs/serve.default.yaml',
                       help='Path to serve config')
    parser.add_argument('--host', type=str, default=None,
                       help='Override host from config')
    parser.add_argument('--port', type=int, default=None,
                       help='Override port from config')
    
    args = parser.parse_args()
    
    # Load config
    config = load_config(args.config)
    
    # Apply overrides
    host = args.host or config.get('host', '0.0.0.0')
    port = args.port or config.get('port', 8080)
    reload = config.get('reload', False)
    
    print(f"Starting CM Expert LLM API server...")
    print(f"  Host: {host}")
    print(f"  Port: {port}")
    print(f"  Reload: {reload}")
    print(f"\nAPI docs will be available at: http://{host}:{port}/docs")
    
    try:
        import uvicorn
        uvicorn.run(
            'cmp_expert.serve.api:app',
            host=host,
            port=port,
            reload=reload
        )
    except ImportError:
        print("Error: uvicorn not installed. Install with: pip install uvicorn fastapi")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
