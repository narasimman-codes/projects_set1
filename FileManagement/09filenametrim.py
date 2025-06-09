import os

def trim_filenames_by_length(folder_path, keep_length):
    """
    Trims filenames in the given folder to a fixed length (excluding extension).
    For example, keeping 11 characters: 'TPF7906_06_1.des' → 'TPF7906_06.des'
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)

            # Skip if filename is already shorter or equal
            if len(name) <= keep_length:
                continue

            # Trim the name
            trimmed_name = name[:keep_length] + ext
            trimmed_path = os.path.join(folder_path, trimmed_name)

            # Avoid overwriting
            counter = 1
            while os.path.exists(trimmed_path):
                trimmed_name = f"{name[:keep_length]}_{counter}{ext}"
                trimmed_path = os.path.join(folder_path, trimmed_name)
                counter += 1

            os.rename(file_path, trimmed_path)
            print(f"Renamed: {filename} → {trimmed_name}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    length = input("Enter the number of characters to keep in the filename (excluding extension): ").strip()

    if os.path.isdir(folder) and length.isdigit():
        trim_filenames_by_length(folder, int(length))
    else:
        print("Invalid folder path or length input.")
