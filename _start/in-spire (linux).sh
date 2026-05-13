#!/bin/bash
# in-spire — methodology dashboard launcher (Linux)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT" || exit 1
if [ ! -f "50_tools/methodology.py" ]; then
  echo "[err] 50_tools/methodology.py not found"
  exit 1
fi
exec /usr/bin/env python3 50_tools/methodology.py dashboard --open
