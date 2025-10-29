#!/bin/bash

# 3DS Decryptor GUI Launcher
# This script launches the GUI for 3DS/CIA decryption

echo "Starting 3DS Decryptor GUI..."

# Check if Wine is installed
if ! command -v wine &> /dev/null; then
    echo "Wine is not installed. Please install it with:"
    echo "sudo pacman -S wine"
    echo "Then run this script again."
    exit 1
fi

# Check if Python3 with tkinter is available
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "Python3 with tkinter is not installed. Please install it with:"
    echo "sudo pacman -S tk"
    echo "Then run this script again."
    exit 1
fi

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Change to the script directory
cd "$SCRIPT_DIR"

# Launch the GUI
python3 decrypt_gui.py