# 3DS/CIA Decryptor - Windows Build Package

## 📦 Package Contents

This package contains everything needed to run the 3DS/CIA Decryptor on Windows:

### 🎮 Main Applications:
- **3DS_Decryptor_GUI** - Standalone executable (Linux build, needs Windows recompile)
- **start_gui_windows.bat** - Python script launcher (requires Python)

### 🔧 Required Tools:
- **decrypt.exe** - Main decryption tool
- **ctrtool.exe** - 3DS title/key tool  
- **makerom.exe** - ROM building tool
- **Batch CIA 3DS Decryptor.bat** - Original batch script

### 📚 Documentation:
- **README_WINDOWS.md** - Windows setup instructions
- **README_GUI.md** - GUI feature documentation
- **BUILD_INSTRUCTIONS.md** - This file

## 🚀 How to Use

### Option 1: Recompile for Windows (Recommended)
1. Install Python 3.7+ on Windows
2. Install PyInstaller: `pip install pyinstaller`
3. Run: `pyinstaller --onefile --windowed --add-data="Batch CIA 3DS Decryptor.bat:." --add-data="decrypt.exe:." --add-data="ctrtool.exe:." --add-data="makerom.exe:." decrypt_gui_windows.py`
4. This will create a proper Windows .exe file

### Option 2: Use Python Script
1. Install Python 3.7+ with tkinter on Windows
2. Double-click `start_gui_windows.bat`
3. Follow the prompts

### Option 3: Use Original Batch Script
1. Double-click `Batch CIA 3DS Decryptor.bat`
2. Place your .3ds/.cia files in the same folder
3. Follow command-line prompts

## 🔨 Building Windows Executable

To create a proper Windows .exe file:

```batch
# Install requirements
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name=3DS_Decryptor_GUI --add-data="Batch CIA 3DS Decryptor.bat:." --add-data="decrypt.exe:." --add-data="ctrtool.exe:." --add-data="makerom.exe:." decrypt_gui_windows.py

# The .exe will be in dist/ folder
```

## 📋 System Requirements

- **Windows 7 or later**
- **For executable:** No additional software required
- **For Python script:** Python 3.7+ with tkinter
- **Disk space:** 2x the size of files being decrypted
- **RAM:** 4GB+ recommended for large files

## 🎯 Features

- ✅ Modern dark-themed GUI
- ✅ File browser with directory memory
- ✅ Real-time decryption progress
- ✅ Copyable log output
- ✅ Automatic file cleanup
- ✅ Original file deletion option
- ✅ Support for .3ds and .cia files
- ✅ Creates decrypted files in original location

## 🐛 Troubleshooting

**"Python not found"**
- Install Python from python.org
- Ensure "Add Python to PATH" is checked during installation

**"tkinter not available"**
- Reinstall Python with tkinter support
- Or use Windows Store version of Python

**"Failed to run decryption"**
- Run as Administrator
- Check all .exe files are in same folder
- Ensure antivirus isn't blocking the tools

**Antivirus warnings**
- Add folder to antivirus exceptions
- The tools may trigger false positives

## 📞 Support

For issues:
1. Check the log output for specific errors
2. Ensure all required files are present
3. Try running as Administrator
4. Check available disk space

---

**Note:** This package was prepared on Linux. For best results, rebuild the executable on Windows using the provided build instructions.