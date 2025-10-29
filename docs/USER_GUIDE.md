# 3DS/CIA Decryptor - User Guide

A modern, cross-platform GUI application for decrypting 3DS and CIA files.

## 🚀 Quick Start

### Linux Users:
1. **AppImage (Recommended):**
   ```bash
   chmod +x 3DS-Decryptor-1.0-x86_64.AppImage
   ./3DS-Decryptor-1.0-x86_64.AppImage
   ```

2. **Python Version:**
   ```bash
   ./scripts/start_gui.sh
   ```

### Windows Users:
1. **Extract Package:** Download and extract `3DS_Decryptor_Windows_v1.0.zip`
2. **Choose Launch Method:**
   - Double-click `start_gui_windows.bat` (Python)
   - Or recompile executable (see Windows setup)

## 🎮 Features

### ✅ Modern Interface
- **Dark theme** with professional styling
- **Emoji icons** for visual appeal
- **Card-based layout** with modern design
- **Responsive interface** that adapts to content

### ✅ User Experience
- **File browser** with directory memory
- **Real-time progress** tracking
- **Copyable logs** for troubleshooting
- **Status indicators** with emojis
- **Automatic cleanup** of temporary files

### ✅ File Management
- **Decrypts to original directory**
- **Automatic cleanup** of temp files
- **Optional original file deletion**
- **Support for .3ds and .cia files**

## 📁 File Support

### Input Files:
- **.3ds files** - 3DS game cartridges
- **.cia files** - Nintendo eShop content (games, DLC, updates)

### Output Files:
- `filename-decrypted.3ds` - Decrypted 3DS games
- `filename-decrypted.cia` - Decrypted CIA games
- `filename (Patch)-decrypted.cia` - Decrypted game updates
- `filename (DLC)-decrypted.cia` - Decrypted DLC
- `filename-decrypted.cci` - Converted CIA files

## 🔧 System Requirements

### Linux:
- **Architecture:** x86_64 (64-bit)
- **Dependencies:** Wine, Python 3.7+, tkinter
- **Disk Space:** 2x file size being decrypted
- **RAM:** 4GB+ recommended for large files

### Windows:
- **OS:** Windows 7 or later
- **Dependencies:** Python 3.7+ (for script version)
- **Disk Space:** 2x file size being decrypted
- **RAM:** 4GB+ recommended for large files

## 🎯 How to Use

### Step 1: Launch Application
- **Linux:** Run AppImage or use start_gui.sh
- **Windows:** Extract package and run launcher

### Step 2: Select File
1. Click **"Browse"** button
2. Navigate to your .3ds or .cia file
3. Select the file and click **"Open"**

### Step 3: Start Decryption
1. Click **"🔓 Start Decryption"** button
2. Watch real-time progress in the log area
3. Wait for completion message

### Step 4: Access Results
- Decrypted files appear in **same directory** as original
- Optional: Click **"🗑️ Delete Original"** to save space

## 🐛 Troubleshooting

### Common Issues:

**"Application won't start"**
- **Linux:** Install Wine (`sudo pacman -S wine`) and Python tkinter (`sudo pacman -S tk`)
- **Windows:** Install Python 3.7+ with tkinter

**"Decryption failed"**
- Ensure all .exe files are present in src/tools/
- Run as Administrator if needed
- Check available disk space

**"File not found" errors**
- Verify file paths don't contain special characters
- Check file permissions (read access)
- Ensure files aren't corrupted

**Antivirus warnings**
- Add application folder to antivirus exceptions
- The decryption tools may trigger false positives

### Log Analysis:
- Use **"📋 Copy"** button to copy error messages
- Check for specific error codes
- Ensure Wine/Python dependencies are met

## 📱 Advanced Features

### Directory Memory:
- Application remembers last used folder
- Settings saved between sessions
- Automatic navigation to recent locations

### Safe Deletion:
- Confirmation dialog before deleting originals
- Only deletes after successful decryption
- Undo not possible (confirm before proceeding)

### Cross-Platform:
- Consistent interface on Linux and Windows
- Same feature set across platforms
- Compatible file formats

## 📞 Getting Help

For additional support:
1. Check the log output for specific errors
2. Verify all dependencies are installed
3. Ensure sufficient disk space is available
4. Try running as Administrator/root if needed

---

**Note:** This tool is for personal use only. Ensure you have legal right to decrypt files you process.