import os
import shutil

def move_files_to_directory(source_directory):
    """Move files from subfolders to the specified directory."""
    file_count = {}  # Dictionary to keep track of filenames and their count

    # Traverse the source directory and its subdirectories
    for root, dirs, files in os.walk(source_directory):
        for filename in files:
            source_file_path = os.path.join(root, filename)
            destination_file_path = os.path.join(source_directory, filename)

            # If file with same name already exists in destination, rename it
            if os.path.exists(destination_file_path):
                file_count.setdefault(filename, 0)
                file_count[filename] += 1
                new_filename = f"{os.path.splitext(filename)[0]}_{file_count[filename]}{os.path.splitext(filename)[1]}"
                destination_file_path = os.path.join(source_directory, new_filename)

            # Move the file to the source directory
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {source_file_path} to {destination_file_path}")

if __name__ == "__main__":
    source_directory = input("Enter source directory path: ")

    move_files_to_directory(source_directory)
