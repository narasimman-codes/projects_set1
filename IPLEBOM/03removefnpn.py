import csv
import os

def remove_strings_in_columns(input_folder, output_folder):
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            input_filepath = os.path.join(input_folder, filename)
            output_filepath = os.path.join(output_folder, filename)
            
            with open(input_filepath, 'r', newline='') as infile, \
                 open(output_filepath, 'w', newline='') as outfile:
                csv_reader = csv.reader(infile)
                csv_writer = csv.writer(outfile)
                
                for row in csv_reader:
                    # Remove "FN" and "PN:" from columns F, G, H, I
                    for index in range(len(row)):
                        if index in [5, 6, 7, 8]:
                            row[index] = row[index].replace("FN", "").replace("PN:", "")
                    
                    csv_writer.writerow(row)
    
    print("Processed files saved to", output_folder)

if __name__ == "__main__":
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")
    remove_strings_in_columns(input_folder, output_folder)
