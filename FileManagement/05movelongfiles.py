import os
import shutil

def move_long_filenames(folder_path, max_length=14):
    """
    Moves files whose full filename (including extension) is longer than max_length
    to a subfolder named 'LongNames' within the same folder.
    """
    long_names_folder = os.path.join(folder_path, "LongNames")
    os.makedirs(long_names_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        source_path = os.path.join(folder_path, filename)

        if os.path.isfile(source_path):
            if len(filename) > max_length:
                destination_path = os.path.join(long_names_folder, filename)

                # Avoid overwriting
                counter = 1
                base_name, ext = os.path.splitext(filename)
                while os.path.exists(destination_path):
                    new_name = f"{base_name}_{counter}{ext}"
                    destination_path = os.path.join(long_names_folder, new_name)
                    counter += 1

                shutil.move(source_path, destination_path)
                print(f"Moved: {filename} → {destination_path}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()

    if os.path.isdir(folder):
        move_long_filenames(folder, max_length=14)
    else:
        print("Invalid folder path. Please try again.")
