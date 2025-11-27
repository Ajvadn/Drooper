#!/bin/bash
# Get the directory where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if venv exists
if [ ! -d "$DIR/venv" ]; then
    echo "[!] Virtual environment not found. Creating one..."
    python3 -m venv "$DIR/venv"
    echo "[*] Installing dependencies..."
    "$DIR/venv/bin/pip" install -r "$DIR/requirements.txt"
fi

# Run the tool using the venv python
"$DIR/venv/bin/python" "$DIR/main.py"
