import os
import shutil
from collections import defaultdict

def move_latest_files_to_native(base_dir):
    if not os.path.isdir(base_dir):
        print("Provided path is not a directory.")
        return

    # Process each folder inside base_dir
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)

        # Skip if not a directory
        if not os.path.isdir(folder_path):
            continue

        print(f"\nProcessing folder: {folder_name}")
        native_files_root = os.path.join(folder_path, "Native Files")
        os.makedirs(native_files_root, exist_ok=True)

        # Dictionary to hold files grouped by name+extension
        file_dict = defaultdict(list)

        # Walk all subdirectories, including Native Files and its subfolders
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_key = file.lower()  # normalize
                file_dict[file_key].append(file_path)

        # Process each group of duplicates
        for file_key, paths in file_dict.items():
            if len(paths) == 1:
                # Only one copy
                src = paths[0]
                dst = os.path.join(native_files_root, os.path.basename(src))
                if os.path.abspath(src) != os.path.abspath(dst):
                    shutil.move(src, dst)
                    print(f"Moved: {src} -> {dst}")
            else:
                # Multiple copies — keep the latest
                paths.sort(key=lambda x: os.path.getmtime(x), reverse=True)
                latest_file = paths[0]
                dst = os.path.join(native_files_root, os.path.basename(latest_file))

                if os.path.abspath(latest_file) != os.path.abspath(dst):
                    shutil.move(latest_file, dst)
                    print(f"Moved latest: {latest_file} -> {dst}")

                # Delete all older versions
                for old_file in paths[1:]:
                    try:
                        os.remove(old_file)
                        print(f"Deleted duplicate: {old_file}")
                    except Exception as e:
                        print(f"Failed to delete {old_file}: {e}")

if __name__ == "__main__":
    base_input = input("Enter the base directory path (contains 523 folders): ").strip()
    move_latest_files_to_native(base_input)
    print("\nOperation complete.")
