import os
import shutil

def move_files_to_native_files(source_directory):
    """
    Move files from all subfolders of source_directory into 'Native Files' subfolder.
    Creates the 'Native Files' folder if it doesn't exist.
    Renames files if duplicates are detected.
    """
    native_files_dir = os.path.join(source_directory, "Native Files")
    os.makedirs(native_files_dir, exist_ok=True)  # Create if doesn't exist

    file_count = {}  # Track duplicate filenames

    for root, dirs, files in os.walk(source_directory):
        # Skip 'Native Files' folder itself
        if native_files_dir in root:
            continue

        for filename in files:
            source_file_path = os.path.join(root, filename)
            destination_file_path = os.path.join(native_files_dir, filename)

            # Rename file if it already exists in the destination
            if os.path.exists(destination_file_path):
                file_count.setdefault(filename, 0)
                file_count[filename] += 1
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{file_count[filename]}{ext}"
                destination_file_path = os.path.join(native_files_dir, new_filename)

            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {source_file_path} → {destination_file_path}")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ").strip()
    if os.path.isdir(source_directory):
        move_files_to_native_files(source_directory)
    else:
        print("Invalid directory path. Please check and try again.")
