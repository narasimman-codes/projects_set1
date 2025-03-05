import os
from openpyxl import load_workbook

def clean_column_delete(ws):
    # Columns V to AB
    ws.delete_cols(22, 8)

    # Columns S, T
    ws.delete_cols(19, 3)

    # Columns H to Q
    ws.delete_cols(8, 10)

    # Column F
    ws.delete_cols(6)



def process_excel_files(input_directory, output_directory):
    if input_directory == output_directory:
        print("Error: Input and output directories should be different.")
        return

    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".xlsx"):
                input_file_path = os.path.join(root, filename)
                output_file_path = input_file_path.replace(input_directory, output_directory)

                # Create the output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                print(f"Processing file: {input_file_path}")

                # Load the workbook
                wb = load_workbook(input_file_path)

                # Apply column deletion and adjustment function to each sheet
                for ws in wb.worksheets:
                    clean_column_delete(ws)

                # Save the modified workbook
                wb.save(output_file_path)
                print("Processed successfully")

# Prompt the user to enter the input and output directory paths
input_directory = input("Enter the input folder directory path: ")
output_directory = input("Enter the output folder directory path: ")

process_excel_files(input_directory, output_directory)
