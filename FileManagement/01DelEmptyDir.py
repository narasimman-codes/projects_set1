import os

def delete_empty_folders(directory):
    """Recursively delete empty folders."""
    for root, dirs, files in os.walk(directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):  # Check if folder is empty
                os.rmdir(folder_path)
                print(f"Deleted empty folder: {folder_path}")
    
    # After deleting empty subfolders, check if parent folder has become empty
    if not os.listdir(directory):
        os.rmdir(directory)
        print(f"Deleted empty folder: {directory}")

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    delete_empty_folders(directory)
