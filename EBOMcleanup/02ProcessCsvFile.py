import os
import pandas as pd

def process_csv_files(input_directory, output_directory):
    if input_directory == output_directory:
        print("Error: Input and output directories should be different.")
        return

    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".csv"):
                input_file_path = os.path.join(root, filename)
                output_file_path = input_file_path.replace(input_directory, output_directory).replace('.csv', '.xlsx')

                # Create the output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                print(f"Processing file: {input_file_path}")

                # Read the CSV file into a DataFrame, skipping the first two rows
                df = pd.read_csv(input_file_path, skiprows=2)

                # Write the DataFrame to Excel format
                df.to_excel(output_file_path, index=False)
                print("Processed successfully")

# Prompt the user to enter the input and output directory paths
input_directory = input("Enter the input folder directory path: ")
output_directory = input("Enter the output folder directory path: ")

process_csv_files(input_directory, output_directory)
