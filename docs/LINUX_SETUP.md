# Linux Setup Guide

## 🐧 Installation Options

### Option 1: AppImage (Recommended)
1. Download `3DS-Decryptor-1.0-x86_64.AppImage`
2. Make executable: `chmod +x 3DS-Decryptor-1.0-x86_64.AppImage`
3. Run: `./3DS-Decryptor-1.0-x86_64.AppImage`

### Option 2: Native Python
1. Install dependencies:
   ```bash
   # Arch Linux
   sudo pacman -S wine tk
   
   # Ubuntu/Debian
   sudo apt install wine python3-tk
   
   # Fedora
   sudo dnf install wine python3-tkinter
   ```

2. Clone repository and run:
   ```bash
   git clone <repository-url>
   cd 3DS-Decryptor-Modern-GUI
   ./scripts/start_gui.sh
   ```

## 📋 Dependencies

### Required:
- **Wine** - For running Windows decryption tools
- **Python 3.7+** - Application runtime
- **tkinter** - GUI framework

### Optional:
- **ImageMagick** - For icon generation (build time only)

## 🔧 Manual Setup

### Wine Configuration:
```bash
# Initialize Wine (first time only)
winecfg

# Set Windows version to Windows 10 for best compatibility
```

### Python Verification:
```bash
# Check Python version
python3 --version

# Verify tkinter
python3 -c "import tkinter; print('tkinter available')"
```

## 🐛 Troubleshooting

### Wine Issues:
```bash
# Check Wine installation
wine --version

# Reset Wine configuration
rm -rf ~/.wine
winecfg
```

### Python Issues:
```bash
# Check tkinter availability
python3 -c "import tkinter"

# Install tkinter if missing
# Arch: sudo pacman -S tk
# Ubuntu: sudo apt install python3-tk
```

### Permission Issues:
```bash
# Make scripts executable
chmod +x scripts/*.sh

# Fix file permissions
chmod 644 src/tools/*.exe
```

### Performance Issues:
- Increase available RAM for large files
- Use SSD storage for better I/O performance
- Close other applications during decryption

## 📁 File Locations

### AppImage:
- **Portable:** Runs from any location
- **Self-contained:** No installation required
- **Settings:** Stored in ~/.local/share/3DS-Decryptor/

### Native:
- **Source:** Current directory
- **Settings:** Stored in ~/.config/3DS-Decryptor/
- **Logs:** Stored in source directory