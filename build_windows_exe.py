#!/usr/bin/env python3
"""
Build script to create Windows executable for 3DS Decryptor GUI
Requires: pip install pyinstaller
"""

import os
import subprocess
import sys

def build_exe():
    """Build Windows executable using PyInstaller"""
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Build command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create single executable
        "--windowed",                   # Hide console window
        "--name=3DS_Decryptor_GUI",      # Name of executable
        "--icon=icon.ico",               # Icon file (if available)
        "--add-data=Batch CIA 3DS Decryptor.bat;.",  # Include batch file
        "--add-data=decrypt.exe;.",      # Include decrypt tool
        "--add-data=ctrtool.exe;.",      # Include ctrtool
        "--add-data=makerom.exe;.",      # Include makerom
        "decrypt_gui_windows.py"
    ]
    
    # Remove icon option if icon file doesn't exist
    if not os.path.exists("icon.ico"):
        cmd = [arg for arg in cmd if not arg.startswith("--icon")]
    
    print("Building Windows executable...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd)
        print("\n✅ Build successful!")
        print("Executable created in: dist/3DS_Decryptor_GUI.exe")
        
        # Create distribution package
        print("\n📦 Creating distribution package...")
        dist_dir = "3DS_Decryptor_Windows"
        
        # Create distribution directory
        if os.path.exists(dist_dir):
            import shutil
            shutil.rmtree(dist_dir)
        os.makedirs(dist_dir)
        
        # Copy executable and required files
        import shutil
        shutil.copy("dist/3DS_Decryptor_GUI.exe", dist_dir)
        shutil.copy("README_GUI.md", dist_dir)
        shutil.copy("README_WINDOWS.md", dist_dir) if os.path.exists("README_WINDOWS.md") else None
        
        print(f"✅ Distribution package created: {dist_dir}/")
        print("You can now distribute this folder to Windows users.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    if build_exe():
        print("\n🎉 Windows executable build completed!")
    else:
        print("\n❌ Build failed. Check the error messages above.")