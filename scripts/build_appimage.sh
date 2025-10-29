#!/bin/bash

# 3DS/CIA Decryptor - AppImage Build Script
# Creates a portable AppImage for Linux distribution

set -e

# Configuration
APP_NAME="3DS-Decryptor"
APP_VERSION="1.0"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/AppImage_build"
APPDIR="${BUILD_DIR}/${APP_NAME}.AppDir"

echo "🔧 Building ${APP_NAME} AppImage v${APP_VERSION}"

# Clean previous build
if [ -d "$BUILD_DIR" ]; then
    echo "🧹 Cleaning previous build..."
    rm -rf "$BUILD_DIR"
fi

# Create AppDir structure
echo "📁 Creating AppDir structure..."
mkdir -p "$APPDIR"
mkdir -p "$APPDIR/usr/bin"
mkdir -p "$APPDIR/usr/lib"
mkdir -p "$APPDIR/usr/share/applications"
mkdir -p "$APPDIR/usr/share/icons/hicolor/256x256/apps"

# Copy application files
echo "📦 Copying application files..."
cp "$SCRIPT_DIR/../src/gui/decrypt_gui.py" "$APPDIR/usr/bin/"
cp "$SCRIPT_DIR/start_gui.sh" "$APPDIR/usr/bin/"
cp "$SCRIPT_DIR/../src/core/batch_cia_3ds_decryptor.sh" "$APPDIR/usr/bin/"
cp "$SCRIPT_DIR/../docs/README_GUI.md" "$APPDIR/usr/share/"
cp "$SCRIPT_DIR/../docs/README_LINUX.md" "$APPDIR/usr/share/"

# Copy decryption tools (if they exist)
echo "🔧 Copying decryption tools..."
if [ -f "$SCRIPT_DIR/../src/core/decrypt.exe" ]; then
    cp "$SCRIPT_DIR/../src/core/decrypt.exe" "$APPDIR/usr/bin/"
fi
if [ -f "$SCRIPT_DIR/../src/core/ctrtool.exe" ]; then
    cp "$SCRIPT_DIR/../src/core/ctrtool.exe" "$APPDIR/usr/bin/"
fi
if [ -f "$SCRIPT_DIR/../src/core/makerom.exe" ]; then
    cp "$SCRIPT_DIR/../src/core/makerom.exe" "$APPDIR/usr/bin/"
fi

# Create desktop file
echo "📄 Creating desktop file..."
cat > "$APPDIR/usr/share/applications/${APP_NAME}.desktop" << EOF
[Desktop Entry]
Version=${APP_VERSION}
Type=Application
Name=3DS/CIA Decryptor
Comment=Modern GUI for decrypting 3DS and CIA files
Exec=3ds-decryptor
Icon=3ds-decryptor
Terminal=false
Categories=Game;Utility;
Keywords=3ds;cia;decrypt;emulator;nintendo;
EOF

# Create icon (simple text-based icon)
echo "🎨 Creating application icon..."
# Create a simple PNG icon using ImageMagick if available, otherwise use a placeholder
if command -v convert &> /dev/null; then
    # Create a simple icon
    convert -size 256x256 xc:'#2b2b2b' \
            -font DejaVu-Sans-Bold -pointsize 24 -fill white -gravity center \
            -annotate +0+0 '3DS\n🎮' \
            "$APPDIR/usr/share/icons/hicolor/256x256/apps/3ds-decryptor.png" 2>/dev/null || \
    echo "⚠️  Could not create icon, using placeholder"
else
    echo "⚠️  ImageMagick not found, skipping icon creation"
fi

# If no icon was created, create a simple placeholder
if [ ! -f "$APPDIR/usr/share/icons/hicolor/256x256/apps/3ds-decryptor.png" ]; then
    echo "📝 Creating placeholder icon file..."
    # Create a simple text-based icon description
    echo "Icon placeholder - Install ImageMagick for proper icon generation" > "$APPDIR/usr/share/icons/hicolor/256x256/apps/3ds-decryptor.png"
fi

# Create AppRun script
echo "🚀 Creating AppRun script..."
cat > "$APPDIR/AppRun" << 'EOF'
#!/bin/bash
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PATH="${HERE}/usr/bin:${PATH}"
export LD_LIBRARY_PATH="${HERE}/usr/lib:${LD_LIBRARY_PATH}"

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

chmod +x "$APPDIR/AppRun"

# Create desktop file in root
cp "$APPDIR/usr/share/applications/${APP_NAME}.desktop" "$APPDIR/"

# Download AppImageTool if not present
APPIMAGETOOL="${SCRIPT_DIR}/appimagetool-x86_64.AppImage"
if [ ! -f "$APPIMAGETOOL" ]; then
    echo "📥 Downloading AppImageTool..."
    wget -O "$APPIMAGETOOL" "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
    chmod +x "$APPIMAGETOOL"
fi

# Build AppImage
echo "🔨 Building AppImage..."
ARCH="$(uname -m)"
OUTPUT="${SCRIPT_DIR}/${APP_NAME}-${APP_VERSION}-${ARCH}.AppImage"

cd "$BUILD_DIR"
export ARCH="$ARCH"
"$APPIMAGETOOL" --appimage-extract-and-run "$APPDIR" "$OUTPUT"

# Clean up build directory
echo "🧹 Cleaning up build files..."
rm -rf "$APPDIR"

echo "✅ AppImage created successfully!"
echo "📦 Output: $OUTPUT"
echo "💡 To run: ./$OUTPUT"
echo "📋 Size: $(du -h "$OUTPUT" | cut -f1)"

# Test the AppImage
echo "🧪 Testing AppImage..."
if [ -f "$OUTPUT" ]; then
    echo "✅ AppImage file created and is executable"
    ls -la "$OUTPUT"
else
    echo "❌ AppImage creation failed"
    exit 1
fi