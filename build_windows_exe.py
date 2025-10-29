#!/usr/bin/env python3
"""
Build script to create Windows executable for 3DS Decryptor GUI
Requires: pip install pyinstaller

This script should be run on Windows to create Windows executable.
On Linux, it will create the build structure but not the final .exe.
"""

import os
import subprocess
import sys
import shutil
import platform

def check_requirements():
    """Check if required files exist"""
    required_files = [
        "decrypt_gui_windows.py",
        "Batch CIA 3DS Decryptor.bat",
        "decrypt.exe",
        "ctrtool.exe", 
        "makerom.exe"
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print("❌ Missing required files:")
        for file in missing:
            print(f"   - {file}")
        return False
    
    return True

def install_pyinstaller():
    """Install PyInstaller if not available"""
    try:
        import PyInstaller
        return True
    except ImportError:
        print("Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install PyInstaller")
            return False

def build_exe():
    """Build Windows executable using PyInstaller"""
    
    print(f"🔧 Building on {platform.system()}...")
    
    # Check requirements
    if not check_requirements():
        return False
    
    # Install PyInstaller
    if not install_pyinstaller():
        return False
    
    # Build command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create single executable
        "--windowed",                   # Hide console window
        "--name=3DS_Decryptor_GUI",      # Name of executable
        "--add-data=Batch CIA 3DS Decryptor.bat:.",  # Include batch file
        "--add-data=decrypt.exe:.",      # Include decrypt tool
        "--add-data=ctrtool.exe:.",      # Include ctrtool
        "--add-data=makerom.exe:.",      # Include makerom
        "decrypt_gui_windows.py"
    ]
    
    # Add icon if available
    if os.path.exists("icon.ico"):
        cmd.insert(-1, "--icon=icon.ico")
        print("📦 Using custom icon: icon.ico")
    else:
        print("ℹ️  No icon.ico found, using default icon")
    
    print("🔨 Building Windows executable...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        # On Linux, we can't build Windows .exe, but we can prepare the structure
        if platform.system() != "Windows":
            print("⚠️  Warning: Building on Linux. Final .exe requires Windows.")
            print("   This will create the build structure for Windows compilation.")
        
        subprocess.check_call(cmd)
        print("\n✅ Build process completed!")
        
        if platform.system() == "Windows":
            print("Executable created: dist/3DS_Decryptor_GUI.exe")
        else:
            print("Build structure created. Run on Windows to generate .exe")
        
        # Create distribution package
        return create_distribution_package()
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False

def create_distribution_package():
    """Create distribution package"""
    print("\n📦 Creating distribution package...")
    dist_dir = "3DS_Decryptor_Windows"
    
    # Create distribution directory
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir)
    
    # Copy files
    files_to_copy = [
        ("README_GUI.md", "README_GUI.md"),
        ("README_WINDOWS.md", "README_WINDOWS.md"),
        ("ICON_README.md", "ICON_README.md"),
        ("start_gui_windows.bat", "start_gui_windows.bat")
    ]
    
    for src, dst in files_to_copy:
        if os.path.exists(src):
            shutil.copy(src, os.path.join(dist_dir, dst))
    
    # Copy executable if it exists (Windows only)
    if os.path.exists("dist/3DS_Decryptor_GUI.exe"):
        shutil.copy("dist/3DS_Decryptor_GUI.exe", dist_dir)
        print(f"✅ Executable copied: {dist_dir}/3DS_Decryptor_GUI.exe")
    else:
        print("ℹ️  No .exe file created (run on Windows to generate)")
    
    # Create build instructions
    instructions = f"""# 3DS Decryptor - Windows Distribution

## Files Included:
- 3DS_Decryptor_GUI.exe - Main application (if built on Windows)
- start_gui_windows.bat - Alternative launcher
- README_WINDOWS.md - Windows setup instructions
- README_GUI.md - General GUI documentation

## To Use:

### Option 1: Executable (Recommended)
1. Double-click `3DS_Decryptor_GUI.exe`
2. Select your 3DS/CIA files
3. Click "Start Decryption"

### Option 2: Python Script
1. Install Python 3.7+ from python.org
2. Double-click `start_gui_windows.bat`
3. Follow the prompts

## Requirements:
- Windows 7 or later
- For Python version: Python 3.7+ with tkinter

## Build Info:
Built on: {platform.system()}
Build date: {subprocess.check_output(['date'], text=True).strip()}
"""
    
    with open(os.path.join(dist_dir, "DISTRIBUTION_README.md"), "w") as f:
        f.write(instructions)
    
    print(f"✅ Distribution package created: {dist_dir}/")
    print("📋 Package contents:")
    for item in os.listdir(dist_dir):
        print(f"   - {item}")
    
    return True

def main():
    """Main build function"""
    print("🎮 3DS/CIA Decryptor - Windows Build Tool")
    print("=" * 50)
    
    if build_exe():
        print("\n🎉 Build process completed successfully!")
        
        if platform.system() == "Windows":
            print("✅ Ready to distribute: 3DS_Decryptor_Windows/")
        else:
            print("⚠️  Build structure created. Run on Windows to generate .exe")
            print("📁 Distribution package prepared: 3DS_Decryptor_Windows/")
    else:
        print("\n❌ Build failed. Check the error messages above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())