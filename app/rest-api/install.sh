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

echo "Installing Python dependencies from app/rest-api/requirements.txt..."
pip install -r app/rest-api/requirements.txt

echo "Installation complete. The Rest API is now ready to use."
echo "To activate the virtual environment, run: 'source venv/bin/activate'."
echo "You can then run the application with: 'uvicorn app.rest-api.main:app --host 0.0.0.0 --port 8080'."
echo "Once running, you can access the API documentation at: 'http://localhost:8080/docs'."
echo "If you encounter any import errors, run: 'export PYTHONPATH=\$PWD'."