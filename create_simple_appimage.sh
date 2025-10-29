#!/bin/bash

# Simple AppImage Creator for 3DS Decryptor
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="3DS-Decryptor"
VERSION="1.0"
ARCH="$(uname -m)"
APPIMAGE_NAME="${APP_NAME}-${VERSION}-${ARCH}.AppImage"

echo "🔧 Creating ${APPIMAGE_NAME}..."

# Create temporary directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Create AppDir structure
mkdir -p "$TEMP_DIR/AppDir/usr/bin"
mkdir -p "$TEMP_DIR/AppDir/usr/share/applications"
mkdir -p "$TEMP_DIR/AppDir/usr/share/doc"

# Copy files
echo "📦 Copying application files..."
cp "$SCRIPT_DIR/decrypt_gui.py" "$TEMP_DIR/AppDir/usr/bin/"
cp "$SCRIPT_DIR/start_gui.sh" "$TEMP_DIR/AppDir/usr/bin/"
cp "$SCRIPT_DIR/batch_cia_3ds_decryptor.sh" "$TEMP_DIR/AppDir/usr/bin/"
cp "$SCRIPT_DIR/decrypt.exe" "$TEMP_DIR/AppDir/usr/bin/"
cp "$SCRIPT_DIR/ctrtool.exe" "$TEMP_DIR/AppDir/usr/bin/"
cp "$SCRIPT_DIR/makerom.exe" "$TEMP_DIR/AppDir/usr/bin/"
cp "$SCRIPT_DIR/README_GUI.md" "$TEMP_DIR/AppDir/usr/share/doc/"
cp "$SCRIPT_DIR/README_LINUX.md" "$TEMP_DIR/AppDir/usr/share/doc/"

# Create desktop file
echo "📄 Creating desktop file..."
cat > "$TEMP_DIR/AppDir/usr/share/applications/${APP_NAME}.desktop" << EOF
[Desktop Entry]
Version=${VERSION}
Type=Application
Name=3DS/CIA Decryptor
Comment=Modern GUI for decrypting 3DS and CIA files
Exec=3ds-decryptor
Icon=3ds-decryptor
Terminal=false
Categories=Game;Utility;
Keywords=3ds;cia;decrypt;emulator;nintendo;
EOF

# Create AppRun
echo "🚀 Creating AppRun..."
cat > "$TEMP_DIR/AppDir/AppRun" << 'EOF'
#!/bin/bash
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PATH="${HERE}/usr/bin:${PATH}"

# Check dependencies
if ! command -v wine &> /dev/null; then
    echo "❌ Wine is not installed. Please install it:"
    echo "   Ubuntu/Debian: sudo apt install wine"
    echo "   Arch: sudo pacman -S wine"
    echo "   Fedora: sudo dnf install wine"
    exit 1
fi

if ! python3 -c "import tkinter" &> /dev/null; then
    echo "❌ Python3 with tkinter is not installed. Please install it:"
    echo "   Ubuntu/Debian: sudo apt install python3-tk"
    echo "   Arch: sudo pacman -S tk"
    echo "   Fedora: sudo dnf install python3-tkinter"
    exit 1
fi

# Launch the GUI
cd "${HERE}/usr/bin"
exec python3 decrypt_gui.py "$@"
EOF

chmod +x "$TEMP_DIR/AppDir/AppRun"

# Copy desktop file to root
cp "$TEMP_DIR/AppDir/usr/share/applications/${APP_NAME}.desktop" "$TEMP_DIR/AppDir/"

# Download runtime if not present
RUNTIME_FILE="$SCRIPT_DIR/runtime-x86_64"
if [ ! -f "$RUNTIME_FILE" ]; then
    echo "📥 Downloading AppImage runtime..."
    wget -O "$RUNTIME_FILE" "https://github.com/AppImage/AppImageKit/releases/download/continuous/runtime-x86_64"
fi

# Create AppImage
echo "🔨 Building AppImage..."
cd "$TEMP_DIR"
ARCHIVE_NAME="${APP_NAME}.AppImage"

# Create the AppImage by concatenating runtime and squashfs
cat "$RUNTIME_FILE" > "$ARCHIVE_NAME"
chmod +x "$ARCHIVE_NAME"

# Create squashfs root
mkdir -p squashfs-root
cp -r AppDir/* squashfs-root/

# Create squashfs filesystem
if command -v mksquashfs &> /dev/null; then
    mksquashfs squashfs-root/ temp.squashfs -noappend -root-owned -no-xattrs -comp xz
    cat temp.squashfs >> "$ARCHIVE_NAME"
    rm -f temp.squashfs
else
    echo "⚠️  mksquashfs not found, creating simple AppImage without compression"
    # Create a simple tar-based AppImage
    cd AppDir
    tar -czf "../appdata.tar.gz" .
    cd ..
    cat appdata.tar.gz >> "$ARCHIVE_NAME"
    rm -f appdata.tar.gz
fi

# Move to final location
mv "$ARCHIVE_NAME" "$SCRIPT_DIR/$APPIMAGE_NAME"

echo "✅ AppImage created: $SCRIPT_DIR/$APPIMAGE_NAME"
echo "💡 To run: ./$APPIMAGE_NAME"
echo "📋 Size: $(du -h "$SCRIPT_DIR/$APPIMAGE_NAME" | cut -f1)"