# 3DS Decryptor Modern GUI

A modern, cross-platform graphical interface for decrypting 3DS CIA and CCI files. Built with Python and Tkinter for ease of use on both Windows and Linux systems.

## Features

- **Modern Dark Theme Interface** - Professional GUI with intuitive design
- **Cross-Platform Support** - Works on Windows and Linux
- **Batch Processing** - Decrypt multiple files at once
- **Real-Time Progress** - Live progress bars and status updates
- **File Validation** - Automatic detection of valid 3DS files
- **Error Handling** - Comprehensive error reporting and logging
- **Portable Versions** - Standalone executables available

## Quick Start

### Windows
1. Download `3DS_Decryptor_Windows.zip` from [Releases](releases/)
2. Extract and run `start_gui_windows.bat`
3. Or run `3DS_Decryptor_GUI.exe` directly

### Linux
1. Download `3DS-Decryptor.AppImage` from [Releases](releases/)
2. Make executable: `chmod +x 3DS-Decryptor.AppImage`
3. Run: `./3DS-Decryptor.AppImage`

### From Source
```bash
# Install dependencies
pip install tkinter

# Run the GUI
python src/gui/decrypt_gui.py  # Linux
python src/gui/decrypt_gui_windows.py  # Windows
```

## Project Structure

```
├── src/
│   ├── gui/           # GUI applications
│   └── core/          # Core decryption scripts
├── scripts/           # Build and launch scripts
├── docs/              # Documentation
├── releases/          # Distribution packages
└── build/             # Build artifacts (gitignored)
```

## Documentation

- [User Guide](docs/USER_GUIDE.md) - Detailed usage instructions
- [Linux Setup](docs/LINUX_SETUP.md) - Linux-specific setup
- [Windows Setup](docs/WINDOWS_SETUP.md) - Windows-specific setup
- [Build Instructions](docs/) - Build from source

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- For Linux: `python3-tk` package

## License

This project is open source. See [LICENSE](LICENSE) for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For issues and questions:
- Check the [User Guide](docs/USER_GUIDE.md)
- Review existing issues
- Create a new issue with detailed information