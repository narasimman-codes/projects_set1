import os
import re
import pandas as pd

def extract_mfr_values(input_file, output_path):
    """
    Extracts unique 5-character mfr values from an SGML file and saves them to an Excel file.

    Parameters:
        input_file (str): Path to the input SGML file.
        output_path (str): Path to the output Excel file or folder.

    Returns:
        None
    """
    try:
        # Read the content of the SGML file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regular expression to find 5-character values within <mfr> tags
        pattern = re.compile(r'<mfr>(.{5})</mfr>')
        matches = pattern.findall(content)

        # Remove duplicates and sort the values
        unique_values = sorted(set(matches))

        # Prepare the output DataFrame
        df = pd.DataFrame(unique_values, columns=['MFR Values'])

        # Determine if the output path includes a file name
        if os.path.isdir(output_path):
            os.makedirs(output_path, exist_ok=True)
            output_file = os.path.join(output_path, 'extracted_mfr_values.xlsx')
        else:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            output_file = output_path

        # Save the DataFrame to an Excel file
        df.to_excel(output_file, index=False)

        print(f"Extraction completed. Results saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output paths
input_file_path = input("Enter the path to the SGML file (including file name): ")
output_path = input("Enter the path to the output Excel file or folder: ")

# Run the extraction function
extract_mfr_values(input_file_path, output_path)
