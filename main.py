import os
import sys

# Make the src/ package importable without installing the project
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from remote_server import mcp

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
