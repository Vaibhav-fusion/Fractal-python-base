#!/usr/bin/env bash
set -euo pipefail
# Simple helper: create a venv, install requirements, and run fractal.py
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

if [ ! -d .venv ]; then
    echo "Creating virtual environment in .venv..."
    python3 -m venv .venv
fi

echo "Activating venv and installing requirements (if any)..."
# shellcheck disable=SC1091
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
if [ -f requirements.txt ]; then
    if [ -s requirements.txt ]; then
        pip install -r requirements.txt
    else
        echo "No packages listed in requirements.txt"
    fi
fi

echo "Running fractal.py..."
python fractal.py
echo "Done. Output: fractal.svg"
