# 3DS/CIA Decryptor - Windows Version

A modern GUI application for decrypting 3DS and CIA files on Windows.

## 🚀 Quick Start

### Option 1: Using the Executable (Recommended)
1. Download `3DS_Decryptor_GUI.exe`
2. Double-click to run
3. Select your .3ds or .cia file
4. Click "Start Decryption"

### Option 2: Using Python Script
1. Install Python 3.7+ from [python.org](https://python.org)
2. Ensure tkinter is included (usually comes with Python)
3. Run: `python decrypt_gui_windows.py`

## 📋 Features

- **Modern Dark Theme GUI** - Easy on the eyes, professional look
- **File Browser** - Navigate easily to your files
- **Real-time Progress** - Watch decryption progress live
- **Copyable Logs** - Copy output for troubleshooting
- **Directory Memory** - Remembers your last used folder
- **Auto-cleanup** - Moves decrypted files to original location
- **Delete Option** - Safely remove original encrypted files

## 🎮 Supported Files

- **.3ds files** - 3DS game cartridges
- **.cia files** - Nintendo eShop content (games, DLC, updates)

## 📁 Output Files

Decrypted files are created in the same directory as the original:

- `filename-decrypted.3ds` - Decrypted 3DS games
- `filename-decrypted.cia` - Decrypted CIA games  
- `filename (Patch)-decrypted.cia` - Decrypted game updates
- `filename (DLC)-decrypted.cia` - Decrypted DLC
- `filename-decrypted.cci` - Converted CIA files

## ⚙️ Requirements

### For Executable Version:
- Windows 7 or later
- No additional software required

### For Python Script Version:
- Python 3.7 or higher
- tkinter (usually included with Python)

## 🔧 Building from Source

To build the executable yourself:

```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
python build_windows_exe.py
```

This creates `dist/3DS_Decryptor_GUI.exe` and a distribution package.

## 🐛 Troubleshooting

### Common Issues:

**"Failed to run decryption script"**
- Ensure all .exe files (decrypt.exe, ctrtool.exe, makerom.exe) are in the same folder
- Run as Administrator if needed

**"File not found" errors**
- Make sure your 3DS/CIA files are not read-only
- Check file paths don't contain special characters

**Antivirus warnings**
- The executable may trigger false positives
- Add to antivirus exceptions if needed

### Log Analysis:
- Use the "Copy Log" button to copy output
- Check for specific error messages
- Ensure you have enough disk space (2x file size recommended)

## 📝 How It Works

1. **File Selection** - Browse and select your encrypted file
2. **Temporary Processing** - File is copied to app directory for decryption
3. **Decryption** - Uses proven tools (decrypt.exe, ctrtool.exe, makerom.exe)
4. **File Return** - Decrypted files are moved back to original location
5. **Cleanup** - Temporary files are automatically removed

## 🛡️ Safety

- **No Internet Required** - Works completely offline
- **No Data Collection** - All processing happens locally
- **Temporary Files Only** - Original files remain untouched unless you choose to delete
- **Confirmation Prompts** - Delete actions require explicit confirmation

## 📞 Support

If you encounter issues:

1. Check the log output for specific error messages
2. Ensure all required files are present
3. Try running as Administrator
4. Check available disk space

## 🔄 Updates

The GUI automatically remembers your settings between sessions:
- Last used directory
- Window position (if supported by your system)

---

**Note:** This tool is for personal use only. Ensure you have the legal right to decrypt the files you process.