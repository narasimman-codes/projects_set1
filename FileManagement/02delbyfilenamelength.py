import os

def process_files_by_length(base_path, required_length):
    if not os.path.exists(base_path):
        print("Input path does not exist.")
        return

    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if not os.path.isdir(folder_path):
            continue

        native_path = os.path.join(folder_path, "Native Files")
        if not os.path.exists(native_path):
            continue

        for root, _, files in os.walk(native_path):
            for file in files:
                file_path = os.path.join(root, file)
                name, ext = os.path.splitext(file)

                # Remove all spaces
                trimmed_name = name.replace(' ', '')

                if len(trimmed_name) == required_length:
                    # Rename only if name has changed
                    if trimmed_name != name:
                        new_file_name = trimmed_name + ext
                        new_file_path = os.path.join(root, new_file_name)

                        # Handle duplicate names
                        if os.path.exists(new_file_path):
                            base = trimmed_name
                            counter = 1
                            while True:
                                new_file_name = f"{base}_{counter}{ext}"
                                new_file_path = os.path.join(root, new_file_name)
                                if not os.path.exists(new_file_path):
                                    break
                                counter += 1

                        os.rename(file_path, new_file_path)
                        print(f"Renamed: {file_path} → {new_file_path}")
                else:
                    # Delete files not matching the required length
                    try:
                        os.remove(file_path)
                        print(f"Deleted (length ≠ {required_length}): {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")

    print(f"\n✅ Done: All files trimmed and checked for length = {required_length}.")

if __name__ == "__main__":
    input_path = input("Enter the input folder path (e.g., C:\\...\\Cleanup): ").strip()
    try:
        required_len = int(input("Enter required filename length (excluding extension): ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit(1)

    process_files_by_length(input_path, required_len)
