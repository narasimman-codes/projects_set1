import os

def delete_files_with_extensions(folder, extensions):
    # Check if the folder exists
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    # Normalize extensions (remove whitespace)
    extensions = [ext.strip() for ext in extensions]

    # Iterate through files in the folder and subfolders
    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    extensions_input = input("Enter file extensions separated by commas (e.g., .txt,.log): ")
    extensions = extensions_input.split(",")
    delete_files_with_extensions(folder, extensions)
    print("Deletion complete.")
