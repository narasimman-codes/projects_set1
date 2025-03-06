import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("500x400")

        self.folder_path = tk.StringVar()
        self.dest_path = tk.StringVar()
        self.file_types = {}

        # Select Source Directory
        tk.Label(root, text="Select Source Directory:").pack(pady=5)
        tk.Entry(root, textvariable=self.folder_path, width=50).pack(pady=5)
        tk.Button(root, text="Browse", command=self.select_folder).pack(pady=5)

        # File Type Selection
        self.file_frame = tk.Frame(root)
        self.file_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        # Delete & Move Buttons
        tk.Button(root, text="Scan Files", command=self.scan_files).pack(pady=5)
        tk.Button(root, text="Delete Selected Files", command=self.delete_files).pack(pady=5)
        
        # Destination Folder
        tk.Label(root, text="Move Remaining Files To:").pack(pady=5)
        tk.Entry(root, textvariable=self.dest_path, width=50).pack(pady=5)
        tk.Button(root, text="Browse", command=self.select_dest_folder).pack(pady=5)
        
        tk.Button(root, text="Move Files", command=self.move_files).pack(pady=5)

        # Status Label
        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=10)

    def select_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.folder_path.set(path)

    def select_dest_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.dest_path.set(path)

    def scan_files(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showerror("Error", "Please select a folder.")
            return
        
        self.file_types.clear()
        for widget in self.file_frame.winfo_children():
            widget.destroy()
        
        file_extensions = set()
        for root, _, files in os.walk(folder):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext:
                    file_extensions.add(ext)

        for ext in sorted(file_extensions):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.file_frame, text=ext, variable=var)
            chk.pack(anchor="w")
            self.file_types[ext] = var

    def delete_files(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showerror("Error", "Please select a folder.")
            return
        
        selected_types = [ext for ext, var in self.file_types.items() if var.get()]
        if not selected_types:
            messagebox.showinfo("Info", "No file types selected for deletion.")
            return
        
        count = 0
        for root, _, files in os.walk(folder):
            for file in files:
                if os.path.splitext(file)[1] in selected_types:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    count += 1

        self.status_label.config(text=f"Deleted {count} files.")
        messagebox.showinfo("Success", f"Deleted {count} files.")

    def move_files(self):
        folder = self.folder_path.get()
        dest = self.dest_path.get()

        if not folder or not dest:
            messagebox.showerror("Error", "Please select both source and destination folders.")
            return

        count = 0
        for root, _, files in os.walk(folder):
            for file in files:
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest, file)

                if os.path.exists(dest_path):
                    # Rename or replace based on latest file
                    if os.path.getmtime(src_path) > os.path.getmtime(dest_path):
                        os.remove(dest_path)
                        shutil.move(src_path, dest_path)
                    else:
                        base, ext = os.path.splitext(file)
                        new_dest = os.path.join(dest, f"{base}_copy{ext}")
                        shutil.move(src_path, new_dest)
                else:
                    shutil.move(src_path, dest_path)
                
                count += 1

        self.status_label.config(text=f"Moved {count} files.")
        messagebox.showinfo("Success", f"Moved {count} files.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
