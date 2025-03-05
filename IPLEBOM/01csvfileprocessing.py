import csv
import os

def delete_row_2_in_csv(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            # Read the contents of the CSV file
            with open(filepath, 'r') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            
            # Check if row 2 exists
            if len(rows) > 1:
                # Delete row 2
                del rows[1]
                
                # Write back to the same file
                with open(filepath, 'w', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
                print(f"Row 2 deleted from {filename}")
            else:
                print(f"No row 2 found in {filename}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    delete_row_2_in_csv(folder_path)
