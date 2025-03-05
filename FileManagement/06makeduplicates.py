import os
import shutil

def duplicate_file(input_file_path, output_directory, num_copies):
    # Extract the filename and extension from the input file path
    filename = os.path.basename(input_file_path)
    file_base, file_extension = os.path.splitext(filename)

    # Check if the filename has at least 7 characters to extract 'TPX1111'
    if len(file_base) < 7:
        raise ValueError("Filename must have at least 7 characters before the extension.")

    # Extract the 'TPX1111' part of the filename
    prefix = file_base[:7]

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Create the duplicate files
    for i in range(1, num_copies + 1):
        # Construct the new filename
        new_filename = f"{prefix}_{i:02d}{file_extension}"
        new_file_path = os.path.join(output_directory, new_filename)
        
        # Copy the original file to the new file path
        shutil.copy(input_file_path, new_file_path)

        print(f"Created: {new_file_path}")

if __name__ == "__main__":
    # Get user inputs
    input_folder = input("Enter the input folder path: ").strip()
    output_folder = input("Enter the output folder path: ").strip()
    num_copies = int(input("Enter the number of copies to create: ").strip())
    
    # List files in the input folder and let the user choose one
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    if not files:
        print("No files found in the input folder.")
    else:
        print("Files in the input folder:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        file_choice = int(input(f"Choose a file to duplicate (1-{len(files)}): ").strip())
        input_file = os.path.join(input_folder, files[file_choice - 1])

        # Duplicate the selected file
        duplicate_file(input_file, output_folder, num_copies)
