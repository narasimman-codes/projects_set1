import os
from collections import defaultdict

def find_duplicates(folder):
    # Dictionary to store files based on their modification time
    files_by_mtime = defaultdict(list)

    # Traverse through the folder and group files by their modification time
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            mtime = os.path.getmtime(file_path)
            files_by_mtime[mtime].append(file_path)

    # Filter out files that have duplicates
    duplicate_files = [files for files in files_by_mtime.values() if len(files) > 1]

    return duplicate_files

def delete_duplicates(duplicate_files):
    # Iterate through duplicate files and retain files with different names
    for files in duplicate_files:
        # Sort files by modification time in descending order
        files.sort(key=os.path.getmtime, reverse=True)
        # Dictionary to store unique filenames
        unique_filenames = {}
        for file_path in files:
            filename = os.path.basename(file_path)
            if filename not in unique_filenames:
                unique_filenames[filename] = file_path
        # Delete files with duplicate names
        for filename, file_path in unique_filenames.items():
            print(f"Retained: {file_path}")
            files.remove(file_path)
        # Delete remaining files
        for file_path in files:
            print(f"Deleting: {file_path}")
            os.remove(file_path)

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    if os.path.exists(folder):
        duplicate_files = find_duplicates(folder)
        delete_duplicates(duplicate_files)
        print("Duplicates deleted successfully.")
    else:
        print("Folder does not exist.")
