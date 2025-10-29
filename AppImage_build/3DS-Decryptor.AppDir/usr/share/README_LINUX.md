# Batch CIA 3DS Decryptor - Linux/Arch Version

## Requirements

### Option 1: Using Wine (Recommended)
Install Wine on Arch Linux:
```bash
sudo pacman -S wine
```

### Option 2: Native Linux Tools
If available, you can replace the Windows executables with native Linux alternatives:
- `ctrtool` - Available in some repositories or can be compiled from source
- `makerom` - May need to be compiled from source
- `decrypt` - Specific 3DS decryption tool

## Usage

1. Install Wine (Option 1) or native tools (Option 2)
2. Place your `.cia` and `.3ds` files in this directory
3. Run the script:
   ```bash
   ./batch_cia_3ds_decryptor.sh
   ```
4. Wait for the process to complete

## Features
- Batch decrypt CIA & 3DS files
- DLC/Patch CIA → Decrypted CIA (installable in Citra)
- 3DS Games → Decrypted and trimmed 3DS (smaller size)
- CIA Games → Decrypted CCI (NCSD), not CXI (NCCH)
- Auto-detect CIA type (DLC/Patch/Game)

## Notes
- The script uses Wine to run the Windows executables by default
- Large files may require significant RAM
- Check `log.txt` for detailed operation logs

## Troubleshooting
- If Wine is not installed, install it with: `sudo pacman -S wine`
- Make sure the script is executable: `chmod +x batch_cia_3ds_decryptor.sh`
- Ensure all .exe files are present in the same directory