import os

def delete_files_with_prefix(folder, prefix):
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    deleted_count = 0

    # Walk through all directories and files
    for root, _, files in os.walk(folder):
        for file in files:
            if file.startswith(prefix):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted_count += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

    if deleted_count:
        print(f"\nTotal files deleted: {deleted_count}")
    else:
        print("No matching files found.")

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    prefix = input("Enter the file name prefix to delete (e.g., Copy_): ")
    delete_files_with_prefix(folder, prefix)
