import os
import tkinter as tk
from tkinter import filedialog, messagebox

def delete_files_with_extension(folder, extension):
    """
    Deletes files with the specified extension in the given folder and its subfolders.
    """
    if not os.path.exists(folder):
        messagebox.showerror("Error", "Folder does not exist.")
        return

    deleted_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                deleted_files.append(file_path)

    if deleted_files:
        messagebox.showinfo("Success", f"Deleted {len(deleted_files)} '{extension}' files.")
    else:
        messagebox.showinfo("Info", f"No '{extension}' files found in the folder.")

def select_folder():
    """
    Opens a folder selection dialog and sets the folder path in the entry field.
    """
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)

def delete_files():
    """
    Handler for the Delete Files button. Retrieves input and calls the deletion function.
    """
    folder = folder_entry.get()
    extension = extension_entry.get()

    if not folder or not extension:
        messagebox.showerror("Error", "Please provide both folder path and file extension.")
        return

    if not extension.startswith("."):
        messagebox.showerror("Error", "File extension must start with a dot (e.g., '.txt').")
        return

    delete_files_with_extension(folder, extension)

# Create the main application window
app = tk.Tk()
app.title("File Deleter")
app.geometry("400x200")

# Folder selection section
folder_label = tk.Label(app, text="Folder Path:")
folder_label.pack(pady=5)

folder_frame = tk.Frame(app)
folder_frame.pack(pady=5, fill=tk.X, padx=10)

folder_entry = tk.Entry(folder_frame, width=40)
folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

browse_button = tk.Button(folder_frame, text="Browse", command=select_folder)
browse_button.pack(side=tk.LEFT, padx=5)

# File extension input section
extension_label = tk.Label(app, text="File Extension (e.g., .txt):")
extension_label.pack(pady=5)

extension_entry = tk.Entry(app)
extension_entry.pack(pady=5)

# Delete files button
delete_button = tk.Button(app, text="Delete Files", command=delete_files, bg="red", fg="white")
delete_button.pack(pady=20)

# Start the Tkinter event loop
app.mainloop()
