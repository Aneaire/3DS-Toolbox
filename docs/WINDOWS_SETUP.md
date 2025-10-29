# Windows Setup Guide

## 🪟 Installation Options

### Option 1: Standalone Executable (Recommended)
1. Download `3DS_Decryptor_Windows_v1.0.zip`
2. Extract to folder (e.g., `C:\3DS-Decryptor\`)
3. Run `3DS_Decryptor_GUI.exe` (after recompilation)

### Option 2: Python Script
1. Install Python 3.7+ from [python.org](https://python.org)
2. Ensure tkinter is included (default with most installations)
3. Extract package to folder
4. Run `start_gui_windows.bat`

### Option 3: Original Batch Script
1. Extract package to folder
2. Place .3ds/.cia files in same directory
3. Run `Batch CIA 3DS Decryptor.bat`

## 🔧 Python Installation

### Download Python:
1. Visit [python.org](https://python.org)
2. Download Python 3.7+ (64-bit recommended)
3. Run installer
4. **Important:** Check "Add Python to PATH" during installation

### Verify Installation:
```cmd
python --version
python -c "import tkinter; print('tkinter available')"
```

## 📋 Dependencies

### Required for Python Version:
- **Python 3.7+** - Application runtime
- **tkinter** - GUI framework (included with Python)

### Required for All Versions:
- **Windows 7 or later** - Operating system
- **4GB+ RAM** - For large file processing
- **2x file size** - Available disk space

## 🎯 Usage Instructions

### Step 1: Launch Application
- **Executable:** Double-click `3DS_Decryptor_GUI.exe`
- **Python:** Double-click `start_gui_windows.bat`
- **Batch:** Double-click `Batch CIA 3DS Decryptor.bat`

### Step 2: Select File
1. Click **"Browse"** button
2. Navigate to your .3ds or .cia file
3. Select file and click **"Open"**

### Step 3: Start Decryption
1. Click **"🔓 Start Decryption"** button
2. Monitor progress in the log area
3. Wait for completion message

### Step 4: Access Results
- Decrypted files appear in **same directory** as original
- Optional: Click **"🗑️ Delete Original"** to save space

## 🐛 Troubleshooting

### Common Issues:

**"Python not found"**
```cmd
# Check Python installation
python --version

# Reinstall with PATH added
# Download from python.org and ensure "Add to PATH" is checked
```

**"tkinter not available"**
```cmd
# Reinstall Python with tkinter support
# Download full Python installer (not windows store version)
```

**"Failed to run decryption"**
- Run as Administrator
- Check all .exe files are present in folder
- Ensure antivirus isn't blocking the tools
- Verify file permissions (not read-only)

**"Access denied" errors**
- Right-click application → "Run as administrator"
- Check User Account Control (UAC) settings
- Ensure folder isn't in protected location

### Antivirus Issues:
Many antivirus programs flag the decryption tools as false positives:

1. **Add Exception:** Add application folder to antivirus exclusions
2. **Temporarily Disable:** Disable antivirus during decryption
3. **Whitelist:** Mark files as safe in antivirus software

### Performance Issues:
- **RAM Usage:** Close other applications for large files
- **Disk Space:** Ensure 2x file size available
- **SSD Storage:** Use SSD for better performance
- **Background Processes:** Close unnecessary programs

## 📁 File Locations

### Default Installation:
```
C:\3DS-Decryptor\
├── 3DS_Decryptor_GUI.exe          # Main application
├── start_gui_windows.bat            # Python launcher
├── Batch CIA 3DS Decryptor.bat   # Original batch script
├── decrypt.exe                      # Decryption tool
├── ctrtool.exe                     # 3DS tool
├── makerom.exe                     # ROM tool
└── docs/                           # Documentation
```

### User Data:
- **Settings:** `%APPDATA%\3DS-Decryptor\`
- **Logs:** Application directory
- **Temp Files:** Application directory (auto-cleaned)

## 🔨 Building Executable

To create a proper Windows .exe file:

```cmd
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name=3DS_Decryptor_GUI --add-data="Batch CIA 3DS Decryptor.bat:." --add-data="decrypt.exe:." --add-data="ctrtool.exe:." --add-data="makerom.exe:." src/gui/decrypt_gui_windows.py

# Output in dist/ folder
```

## 📱 Integration

### Desktop Shortcut:
1. Right-click `3DS_Decryptor_GUI.exe`
2. Select "Send to" → "Desktop (create shortcut)"
3. Rename shortcut as desired

### Start Menu:
1. Copy application folder to `C:\Program Files\`
2. Right-click executable → "Send to" → "Desktop"
3. Drag shortcut to Start Menu

## 📞 Support

For issues:
1. Check log output for specific error messages
2. Ensure all dependencies are installed
3. Try running as Administrator
4. Verify sufficient disk space
5. Check antivirus settings

### Log Collection:
- Use **"📋 Copy"** button in application
- Paste into text editor for analysis
- Include error messages and system info

---

**Note:** This tool works completely offline and does not collect any user data.