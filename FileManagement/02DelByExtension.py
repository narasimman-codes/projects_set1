import os

def delete_files_with_extension(folder, extension):
    # Check if the folder exists
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    # Iterate through files in the folder
    for root, _, files in os.walk(folder):
        for file in files:
            # Check if the file has the specified extension
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    extension = input("Enter the file extension (e.g., '.txt', '.jpg'): ")
    delete_files_with_extension(folder, extension)
    print(f"All {extension} files deleted successfully.")
