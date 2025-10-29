#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os
import threading
import sys
import json

class Decrypt3DSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("3DS/CIA Decryptor - Windows")
        self.root.geometry("700x650")
        self.root.configure(bg='#2b2b2b')
        
        # Modern color scheme
        self.colors = {
            'bg': '#2b2b2b',
            'fg': '#ffffff',
            'button_bg': '#404040',
            'button_fg': '#ffffff',
            'button_active': '#505050',
            'accent': '#4a9eff',
            'success': '#4caf50',
            'error': '#f44336',
            'warning': '#ff9800',
            'log_bg': '#1e1e1e',
            'log_fg': '#e0e0e0'
        }
        
        # Variables
        self.selected_file = tk.StringVar()
        self.decryptor_path = os.path.dirname(os.path.abspath(__file__))
        self.last_directory = os.path.expanduser("~")  # Start with home directory
        self.config_file = os.path.join(self.decryptor_path, "gui_config.json")
        self.current_file_path = None  # Track current file for deletion
        
        # Load last directory from config
        self.load_config()
        
        # Configure root window
        self.root.tk_setPalette(background=self.colors['bg'], 
                               foreground=self.colors['fg'],
                               activeBackground=self.colors['button_active'],
                               activeForeground=self.colors['fg'])
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title with modern styling
        title_frame = tk.Frame(main_container, bg=self.colors['bg'])
        title_frame.pack(fill="x", pady=(0, 20))
        
        title_label = tk.Label(title_frame, text="🎮 3DS/CIA File Decryptor (Windows)", 
                              font=("Segoe UI", 20, "bold"),
                              bg=self.colors['bg'], fg=self.colors['fg'])
        title_label.pack()
        
        subtitle = tk.Label(title_frame, text="Decrypt your 3DS games and CIA files easily", 
                           font=("Segoe UI", 10),
                           bg=self.colors['bg'], fg='#888888')
        subtitle.pack(pady=(5, 0))
        
        # File selection card
        file_card = tk.Frame(main_container, bg=self.colors['button_bg'], relief="flat", bd=0)
        file_card.pack(fill="x", pady=10, ipady=15, ipadx=15)
        
        file_label = tk.Label(file_card, text="📁 Select File:", 
                             font=("Segoe UI", 11, "bold"),
                             bg=self.colors['button_bg'], fg=self.colors['fg'])
        file_label.pack(anchor="w", padx=15, pady=(0, 8))
        
        # File input frame
        file_input_frame = tk.Frame(file_card, bg=self.colors['button_bg'])
        file_input_frame.pack(fill="x", padx=15, pady=(0, 10))
        
        file_entry = tk.Entry(file_input_frame, textvariable=self.selected_file, 
                             font=("Segoe UI", 10),
                             bg='#1e1e1e', fg=self.colors['fg'],
                             insertbackground=self.colors['accent'],
                             relief="flat", bd=5)
        file_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        browse_btn = tk.Button(file_input_frame, text="Browse", command=self.browse_file,
                              font=("Segoe UI", 10, "bold"),
                              bg=self.colors['accent'], fg=self.colors['fg'],
                              activebackground='#3a8eef', relief="flat", bd=0,
                              padx=20, pady=8)
        browse_btn.pack(side="right")
        
        # Action buttons
        button_frame = tk.Frame(main_container, bg=self.colors['bg'])
        button_frame.pack(fill="x", pady=15)
        
        decrypt_btn = tk.Button(button_frame, text="🔓 Start Decryption", command=self.start_decryption,
                               font=("Segoe UI", 12, "bold"),
                               bg=self.colors['success'], fg=self.colors['fg'],
                               activebackground='#45a049', relief="flat", bd=0,
                               padx=30, pady=12)
        decrypt_btn.pack()
        
        # Delete original file button (initially hidden)
        self.delete_frame = tk.Frame(main_container, bg=self.colors['bg'])
        self.delete_btn = tk.Button(self.delete_frame, text="🗑️ Delete Original Encrypted File", 
                                   command=self.delete_original_file,
                                   font=("Segoe UI", 10, "bold"),
                                   bg=self.colors['error'], fg=self.colors['fg'],
                                   activebackground='#d32f2f', relief="flat", bd=0,
                                   padx=20, pady=8)
        
        # Progress indicator
        self.progress_label = tk.Label(main_container, text="✅ Ready to decrypt", 
                                      font=("Segoe UI", 11),
                                      bg=self.colors['bg'], fg=self.colors['success'])
        self.progress_label.pack(pady=10)
        
        # Log section
        log_frame = tk.Frame(main_container, bg=self.colors['bg'])
        log_frame.pack(fill="both", expand=True, pady=(10, 0))
        
        log_header = tk.Frame(log_frame, bg=self.colors['bg'])
        log_header.pack(fill="x", pady=(0, 8))
        
        log_label = tk.Label(log_header, text="📋 Output Log", 
                            font=("Segoe UI", 11, "bold"),
                            bg=self.colors['bg'], fg=self.colors['fg'])
        log_label.pack(side="left")
        
        # Log controls
        log_controls = tk.Frame(log_header, bg=self.colors['bg'])
        log_controls.pack(side="right")
        
        copy_btn = tk.Button(log_controls, text="📋 Copy", command=self.copy_log,
                            font=("Segoe UI", 9),
                            bg=self.colors['button_bg'], fg=self.colors['fg'],
                            activebackground=self.colors['button_active'], relief="flat", bd=0,
                            padx=10, pady=4)
        copy_btn.pack(side="left", padx=2)
        
        clear_btn = tk.Button(log_controls, text="🧹 Clear", command=self.clear_log,
                             font=("Segoe UI", 9),
                             bg=self.colors['button_bg'], fg=self.colors['fg'],
                             activebackground=self.colors['button_active'], relief="flat", bd=0,
                             padx=10, pady=4)
        clear_btn.pack(side="left", padx=2)
        
        # Log text area with modern styling
        log_container = tk.Frame(log_frame, bg=self.colors['button_bg'], relief="flat", bd=0)
        log_container.pack(fill="both", expand=True)
        
        self.log_text = scrolledtext.ScrolledText(log_container, height=12, wrap=tk.WORD,
                                                 font=("Consolas", 9),
                                                 bg=self.colors['log_bg'], fg=self.colors['log_fg'],
                                                 insertbackground=self.colors['accent'],
                                                 relief="flat", bd=0,
                                                 padx=10, pady=10)
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="🚀 Status: Ready", 
                                   font=("Segoe UI", 9),
                                   bg=self.colors['button_bg'], fg=self.colors['fg'],
                                   relief="flat", bd=1, anchor="w", padx=10, pady=3)
        self.status_bar.pack(side="bottom", fill="x")
        
    def load_config(self):
        """Load the last used directory from config file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.last_directory = config.get('last_directory', os.path.expanduser("~"))
                    if not os.path.exists(self.last_directory):
                        self.last_directory = os.path.expanduser("~")
        except Exception:
            self.last_directory = os.path.expanduser("~")
            
    def save_config(self):
        """Save the last used directory to config file"""
        try:
            config = {'last_directory': self.last_directory}
            with open(self.config_file, 'w') as f:
                json.dump(config, f)
        except Exception:
            pass
            
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select 3DS or CIA file",
            initialdir=self.last_directory,
            filetypes=[("3DS files", "*.3ds"), ("CIA files", "*.cia"), ("All files", "*.*")]
        )
        if file_path:
            self.selected_file.set(file_path)
            # Update and save the last used directory
            self.last_directory = os.path.dirname(file_path)
            self.save_config()
            
    def copy_log(self):
        """Copy all log text to clipboard"""
        try:
            self.log_text.tag_add(tk.SEL, "1.0", tk.END)
            self.log_text.mark_set(tk.INSERT, "1.0")
            self.log_text.see(tk.INSERT)
            self.root.clipboard_clear()
            self.root.clipboard_append(self.log_text.get("1.0", tk.END))
            self.log_text.tag_remove(tk.SEL, "1.0", tk.END)
            self.status_bar.config(text="📋 Status: Log copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy log: {str(e)}")
            
    def clear_log(self):
        """Clear the log text"""
        self.log_text.delete("1.0", tk.END)
        self.status_bar.config(text="🧹 Status: Log cleared")
        
    def log_message(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
        
    def start_decryption(self):
        file_path = self.selected_file.get()
        
        if not file_path:
            messagebox.showerror("Error", "Please select a file to decrypt!")
            return
            
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Selected file does not exist!")
            return
            
        if not os.path.exists(self.decryptor_path):
            messagebox.showerror("Error", f"Decryptor path not found: {self.decryptor_path}")
            return
            
        # Hide delete button when starting new decryption
        self.delete_frame.pack_forget()
        
        # Track current file for potential deletion
        self.current_file_path = file_path
            
        # Start decryption in a separate thread
        self.progress_label.config(text="⏳ Decrypting...", fg=self.colors['warning'])
        self.status_bar.config(text="🔄 Status: Decrypting...")
        
        thread = threading.Thread(target=self.decrypt_file, args=(file_path,))
        thread.daemon = True
        thread.start()
        
    def decrypt_file(self, file_path):
        try:
            self.log_message(f"Starting decryption of: {os.path.basename(file_path)}")
            
            # Get original file info
            original_dir = os.path.dirname(file_path)
            filename = os.path.basename(file_path)
            
            # Change to decryptor directory
            os.chdir(self.decryptor_path)
            
            # Copy file to decryptor directory for processing
            self.log_message(f"Copying file to decryptor directory...")
            subprocess.run(['copy', file_path, self.decryptor_path], shell=True, check=True)
            
            # Run the Windows batch script
            self.log_message("Running decryption script...")
            process = subprocess.run(
                ['Batch CIA 3DS Decryptor.bat'],
                capture_output=True,
                text=True,
                shell=True
            )
            
            # Display output
            if process.stdout:
                self.log_message(process.stdout)
            if process.stderr:
                self.log_message(f"Error: {process.stderr}")
                
            if process.returncode == 0:
                self.log_message("Decryption completed successfully!")
                self.progress_label.config(text="Moving decrypted files...", fg=self.colors['warning'])
                
                # Move decrypted files back to original directory
                base_name = os.path.splitext(filename)[0]
                moved_files = []
                
                for ext in ['.3ds', '.cia', '.cci']:
                    pattern = f"{base_name}*decrypted*{ext}"
                    for file in os.listdir('.'):
                        if file.startswith(base_name) and 'decrypted' in file and file.endswith(ext):
                            source_path = os.path.join(self.decryptor_path, file)
                            dest_path = os.path.join(original_dir, file)
                            
                            # Move file back to original directory
                            subprocess.run(['move', source_path, dest_path], shell=True, check=True)
                            moved_files.append(file)
                            self.log_message(f"Moved: {file} -> {original_dir}")
                
                # Clean up copied original file
                original_copy = os.path.join(self.decryptor_path, filename)
                if os.path.exists(original_copy):
                    subprocess.run(['del', original_copy], shell=True, check=True)
                    self.log_message(f"Cleaned up temporary file: {filename}")
                
                self.progress_label.config(text="✅ Decryption Complete!", fg=self.colors['success'])
                self.status_bar.config(text="✅ Status: Complete")
                
                # Show delete button for original file
                self.delete_frame.pack(pady=5)
                
                # Show success message with info about output files
                self.show_decrypted_files(filename, original_dir, moved_files)
            else:
                self.log_message(f"Decryption failed with return code: {process.returncode}")
                self.progress_label.config(text="❌ Decryption Failed!", fg=self.colors['error'])
                self.status_bar.config(text="❌ Status: Failed")
                
        except Exception as e:
            self.log_message(f"❌ Error during decryption: {str(e)}")
            self.progress_label.config(text="❌ Decryption Failed!", fg=self.colors['error'])
            self.status_bar.config(text="❌ Status: Error")
            
    def show_decrypted_files(self, original_filename, original_dir, moved_files):
        if moved_files:
            file_list = '\n'.join([f"• {f}" for f in moved_files])
            messagebox.showinfo("Decryption Complete", 
                              f"Decryption completed!\n\nDecrypted files:\n{file_list}\n\nFiles are located in:\n{original_dir}")
        else:
            messagebox.showinfo("Decryption Complete", 
                              "Decryption completed!\n\nNo decrypted files found.")
                              
    def delete_original_file(self):
        """Delete the original encrypted file after successful decryption"""
        if not self.current_file_path or not os.path.exists(self.current_file_path):
            messagebox.showerror("Error", "Original file not found!")
            return
            
        # Confirm deletion
        filename = os.path.basename(self.current_file_path)
        result = messagebox.askyesno("Confirm Delete", 
                                     f"Are you sure you want to delete the original encrypted file?\n\n{filename}\n\nThis action cannot be undone!")
        
        if result:
            try:
                os.remove(self.current_file_path)
                self.log_message(f"Deleted original file: {filename}")
                self.status_bar.config(text="🗑️ Status: Original file deleted")
                
                # Clear the file selection and hide delete button
                self.selected_file.set("")
                self.delete_frame.pack_forget()
                self.current_file_path = None
                
                messagebox.showinfo("Success", f"Original file deleted successfully:\n{filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete file:\n{str(e)}")
                self.log_message(f"❌ Error deleting file: {str(e)}")

def main():
    root = tk.Tk()
    app = Decrypt3DSGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()