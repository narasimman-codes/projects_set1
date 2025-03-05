import os

def trim_filenames(folder_path, num_characters):
    # Check if the provided folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return

    # List all files in the specified folder
    files = os.listdir(folder_path)
    
    # Filter out only .iso files
    iso_files = [f for f in files if f.endswith('.iso')]
    
    # Trim filenames
    for filename in iso_files:
        # Extract the base filename without the extension
        base_name = filename[:-4]  # Removing the .iso part
        
        # Trim the base name to the desired length
        trimmed_base_name = base_name[:num_characters]
        
        # Generate new filename with the trimmed base name
        new_filename = trimmed_base_name + '.iso'
        
        # Create full old and new file paths
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: '{old_file_path}' to '{new_file_path}'")
        
    print("Renaming completed.")

# Take folder path and number of characters to keep as inputs
folder_path = input("Enter the folder path: ")
num_characters = 10  # The number of characters to keep from the start of the filename

# Call the function to trim filenames
trim_filenames(folder_path, num_characters)
