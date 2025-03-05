import csv
import os

def combine_csv_files(input_folder, output_folder):
    combined_data = []
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_folder, filename)
            # Read the contents of the CSV file
            with open(filepath, 'r') as file:
                csv_reader = csv.reader(file)
                # Skip header if exists except for the first file
                if combined_data:
                    next(csv_reader, None)
                for row in csv_reader:
                    # Skip empty rows
                    if any(row):
                        combined_data.append(row)
    
    # Write combined data to a new CSV file in the output folder
    output_filepath = os.path.join(output_folder, "combined_data.csv")
    with open(output_filepath, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(combined_data)
    
    print("Combined data saved to", output_filepath)

if __name__ == "__main__":
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")
    combine_csv_files(input_folder, output_folder)
