import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from mcp_library_server.server import main

if __name__ == "__main__":
    main()