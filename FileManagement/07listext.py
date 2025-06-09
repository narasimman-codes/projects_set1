import os

def list_extensions(folder):
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    extension_set = set()

    # Walk through the directory
    for root, _, files in os.walk(folder):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext:  # Exclude files with no extension
                extension_set.add(ext.lower())

    # Sort and display
    sorted_extensions = sorted(extension_set)
    if sorted_extensions:
        print("\nAvailable file extensions:")
        for idx, ext in enumerate(sorted_extensions, start=1):
            print(f"{idx}. {ext}")
    else:
        print("No files with extensions found in the folder.")

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    list_extensions(folder)
