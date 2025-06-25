import os
import shutil
from collections import defaultdict

def clean_native_files(folder_path):
    native_dir = os.path.join(folder_path, "Native Files")
    if not os.path.exists(native_dir):
        return

    print(f"\nCleaning Native Files in: {native_dir}")

    # Group files by base name (ignore extension)
    base_name_dict = defaultdict(list)

    for root, _, files in os.walk(native_dir):
        for file in files:
            file_path = os.path.join(root, file)
            base_name = os.path.splitext(file)[0].lower()  # Normalize and remove extension
            base_name_dict[base_name].append(file_path)

    for base, file_list in base_name_dict.items():
        if len(file_list) == 1:
            continue  # No duplicates

        # Sort by modified time, descending
        file_list.sort(key=lambda f: os.path.getmtime(f), reverse=True)
        keep_file = file_list[0]
        print(f"Keeping: {keep_file}")

        for old_file in file_list[1:]:
            try:
                os.remove(old_file)
                print(f"Deleted duplicate: {old_file}")
            except Exception as e:
                print(f"Failed to delete {old_file}: {e}")

def process_all_native_folders(base_dir):
    if not os.path.isdir(base_dir):
        print("Invalid base directory.")
        return

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(folder_path):
            clean_native_files(folder_path)

if __name__ == "__main__":
    base_path = input("Enter the base directory path (contains 523 folders): ").strip()
    process_all_native_folders(base_path)
    print("\nNative Files cleanup complete.")
