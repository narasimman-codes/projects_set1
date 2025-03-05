import os
from natsort import natsorted

def add_prefix_with_incremental_number(folder_path, prefix):
    # Check if the provided folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return
    
    # List all files in the specified folder
    files = os.listdir(folder_path)
    
    # Filter out only .iso files
    iso_files = [f for f in files if f.endswith('.iso')]
    
    if not iso_files:
        print("No .iso files found in the specified folder.")
        return

    # Sort files naturally
    iso_files = natsorted(iso_files)

    # Initialize the incremental number
    increment = 1
    
    # Preview renaming changes
    print("The following changes will be made:")
    for filename in iso_files:
        base_name = filename[:-4]  # Removing the .iso part
        new_filename = f"{prefix}_{increment:02d}_{base_name}.iso"
        print(f"'{filename}' -> '{new_filename}'")
        increment += 1
    
    # Confirm with the user before renaming
    confirm = input("Do you want to proceed with renaming? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Renaming aborted.")
        return

    # Reset incremental number for actual renaming
    increment = 1

    # Add prefix to each .iso file
    for filename in iso_files:
        base_name = filename[:-4]
        new_filename = f"{prefix}_{increment:02d}_{base_name}.iso"
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: '{old_file_path}' to '{new_file_path}'")
        increment += 1
    
    print("Renaming completed.")

# Take folder path and prefix as inputs
folder_path = input("Enter the folder path: ").strip()
prefix = input("Enter the prefix to add: ").strip()

# Call the function to add prefix and incremental number to .iso files
add_prefix_with_incremental_number(folder_path, prefix)
