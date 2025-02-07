#!/bin/bash
set -e

cd "$(dirname "$0")/../.."

echo "Updating package lists..."
sudo apt-get update

echo "Installing required packages: Python 3 and pip..."
sudo apt-get install -y python3 python3-pip

if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating a new virtual environment..."
    python3 -m venv venv
fi

echo "Activating the virtual environment..."
source venv/bin/activate

echo "Upgrading pip to the latest version..."
pip install --upgrade pip

echo "Installing Python dependencies from app/requirements.txt..."
pip install -r app/requirements.txt

echo "Installing Python dependencies from app/cli/requirements.txt..."
pip install -r app/cli/requirements.txt

echo "Making the CLI script executable..."
chmod +x app/cli/main.py

echo "Installation complete. The CLI tool is now ready to use."
echo "To activate the virtual environment, run: 'source venv/bin/activate'."
echo "You can then execute the CLI script with: 'python app/cli/main.py'."
echo "If you encounter any import errors, run: 'export PYTHONPATH=\$PWD'."
