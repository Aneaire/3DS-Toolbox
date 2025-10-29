# 3DS/CIA Decryptor - AppImage Version

A portable, self-contained AppImage for Linux that runs on most distributions without installation.

## 🚀 Quick Start

### Download and Run:
1. Download `3DS-Decryptor-1.0-x86_64.AppImage` (5.3MB)
2. Make it executable: `chmod +x 3DS-Decryptor-1.0-x86_64.AppImage`
3. Run it: `./3DS-Decryptor-1.0-x86_64.AppImage`

That's it! No installation required.

## ✨ Features

- **🎮 Modern GUI** - Dark-themed interface with emoji icons
- **📁 File Browser** - Navigate easily to your 3DS/CIA files
- **⚡ Real-time Progress** - Watch decryption happen live
- **📋 Copyable Logs** - Copy output for troubleshooting
- **💾 Directory Memory** - Remembers your last used folder
- **🗑️ Safe Deletion** - Option to delete original encrypted files
- **🔄 Auto-cleanup** - Moves decrypted files to original location

## 📋 System Requirements

### Minimum Requirements:
- **Linux** (x86_64) - Ubuntu, Fedora, Arch, openSUSE, etc.
- **Wine** - For running Windows decryption tools
- **Python 3.7+ with tkinter** - Usually pre-installed

### Installing Dependencies:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install wine python3-tk
```

**Arch Linux:**
```bash
sudo pacman -S wine tk
```

**Fedora:**
```bash
sudo dnf install wine python3-tkinter
```

## 🎯 Usage

1. **Launch AppImage** - Double-click or run from terminal
2. **Browse Files** - Click "Browse" to select .3ds or .cia files
3. **Start Decryption** - Click "🔓 Start Decryption"
4. **Monitor Progress** - Watch real-time output in the log
5. **Get Results** - Decrypted files appear in original directory

## 📁 File Support

### Input Files:
- **.3ds** - 3DS game cartridges
- **.cia** - Nintendo eShop content (games, DLC, updates)

### Output Files:
- **filename-decrypted.3ds** - Decrypted 3DS games
- **filename-decrypted.cia** - Decrypted CIA games
- **filename (Patch)-decrypted.cia** - Decrypted game updates
- **filename (DLC)-decrypted.cia** - Decrypted DLC
- **filename-decrypted.cci** - Converted CIA files

## 🔧 How AppImage Works

### Self-Contained:
- **No installation** required
- **All dependencies** bundled (except system-level)
- **Portable** - Runs from USB drive
- **Isolated** - Won't interfere with system files

### Security:
- **Read-only** filesystem (except for user files)
- **Sandboxed** from system applications
- **No root** required
- **Offline** operation (no internet needed)

## 🐛 Troubleshooting

### "Permission Denied"
```bash
chmod +x 3DS-Decryptor-1.0-x86_64.AppImage
```

### "Wine Not Found"
Install Wine using your distribution's package manager (see requirements above)

### "Python/tkinter Not Found"
Install Python with tkinter support (see requirements above)

### "AppImage Won't Start"
1. Check dependencies are installed
2. Try running from terminal: `./3DS-Decryptor-1.0-x86_64.AppImage`
3. Check terminal output for error messages

### Antivirus Issues
AppImages may trigger false positives. Add to exceptions if needed.

## 📱 Integration

### Desktop Integration (Optional):
```bash
# Install to applications menu
./3DS-Decryptor-1.0-x86_64.AppImage --install-appimage

# Create desktop shortcut
./3DS-Decryptor-1.0-x86_64.AppImage --desktop-file
```

### Remove Integration:
```bash
./3DS-Decryptor-1.0-x86_64.AppImage --remove-appimage
```

## 🔄 Updates

To update the AppImage:
1. Download new version
2. Replace old AppImage file
3. Settings and configuration are preserved automatically

## 📊 Technical Details

- **Size:** 5.3MB compressed
- **Architecture:** x86_64 (64-bit)
- **Format:** AppImage (self-contained)
- **Dependencies:** Wine, Python3, tkinter (system-level)
- **Isolation:** AppImage runtime sandbox

## 🎮 Compatibility

### Tested Distributions:
- ✅ Ubuntu 20.04+
- ✅ Fedora 35+
- ✅ Arch Linux
- ✅ openSUSE Leap 15.4+
- ✅ Debian 11+
- ✅ Linux Mint 20+

### Should work on most modern Linux distributions with:
- glibc 2.17+
- x86_64 architecture
- Basic graphics system (X11 or Wayland)

## 📞 Support

For issues:
1. Check terminal output when running AppImage
2. Verify Wine and Python dependencies
3. Ensure sufficient disk space (2x file size)
4. Check file permissions

---

**Note:** This AppImage contains all necessary tools and requires no installation. Just download, make executable, and run!