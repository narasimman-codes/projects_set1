import os

def trim_csv_filenames(directory):
    renamed_files = set()  # Set to keep track of renamed filenames
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".csv"):
                # Splitting the filename by "__" to separate the parts
                parts = filename.split("__")
                # Assuming the first part contains the relevant information
                if len(parts) >= 2:
                    # Constructing the new filename
                    new_filename = parts[0] + ".csv"
                    # Check for duplicates
                    if new_filename in renamed_files:
                        # If duplicate, modify the new filename
                        basename, ext = os.path.splitext(new_filename)
                        counter = 1
                        while f"{basename}_duplicate{counter}{ext}" in renamed_files:
                            counter += 1
                        new_filename = f"{basename}_duplicate{counter}{ext}"
                    # Add the new filename to the set
                    renamed_files.add(new_filename)
                    # Renaming the file
                    src_path = os.path.join(root, filename)
                    dst_path = os.path.join(root, new_filename)
                    if src_path != dst_path:
                        os.rename(src_path, dst_path)
                        print(f"Renamed '{filename}' to '{new_filename}'")
                    else:
                        print(f"Skipped renaming '{filename}' as it would result in the same filename")

# Prompt the user to enter the directory path
directory_path = input("Enter the folder directory path: ")

trim_csv_filenames(directory_path)