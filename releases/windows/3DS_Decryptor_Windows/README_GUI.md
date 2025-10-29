# 3DS/CIA Decryptor - Complete Package

This directory contains everything you need to decrypt 3DS and CIA files on Linux.

## Files Included

### Core Decryption Tools
- `decrypt.exe` - Main decryption tool (runs via Wine)
- `ctrtool.exe` - 3DS title/key tool (runs via Wine)
- `makerom.exe` - ROM building tool (runs via Wine)
- `batch_cia_3ds_decryptor.sh` - Linux batch decryption script

### GUI Interface
- `decrypt_gui.py` - Python GUI application for easy file selection and decryption
- `start_gui.sh` - Launcher script for the GUI
- `3DS-Decryptor.desktop` - Desktop entry file

### Documentation
- `README_LINUX.md` - Linux setup instructions
- `README_GUI.md` - This file
- `readme.txt` - Original readme
- `log.txt` - Decryption log file

## How to Use

### Method 1: GUI (Recommended)
1. Double-click `start_gui.sh` or run: `./start_gui.sh`
2. Click "Browse" to select your .3ds or .cia file
3. Click "Start Decryption"
4. Wait for completion and check for decrypted files

### Method 2: Command Line
1. Place your .3ds or .cia files in this directory
2. Run: `./batch_cia_3ds_decryptor.sh`
3. Follow the prompts

### Method 3: Desktop Entry
1. Copy `3DS-Decryptor.desktop` to your desktop
2. Double-click to launch the GUI

## Requirements

- **Wine** (for running Windows executables): `sudo pacman -S wine`
- **Python3 with tkinter** (for GUI): `sudo pacman -S tk`

## Output Files

Decrypted files will be created in this directory with names like:
- `filename-decrypted.3ds` (for 3DS files)
- `filename-decrypted.cia` (for CIA games)
- `filename (Patch)-decrypted.cia` (for patches)
- `filename (DLC)-decrypted.cia` (for DLC)
- `filename-decrypted.cci` (converted CIA files)

## Troubleshooting

- If Wine is not found, install it with: `sudo pacman -S wine`
- If GUI doesn't start, install tkinter with: `sudo pacman -S tk`
- Check `log.txt` for detailed decryption logs
- Make sure all .exe files are present and executable

## Notes

- Large files may require significant RAM
- The GUI automatically copies files to this directory for decryption
- Decrypted CIA files can be installed in Citra emulator
- Decrypted 3DS files are smaller (trimmed) than originals