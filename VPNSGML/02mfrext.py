import re
import pandas as pd

# Function to extract data between <mfr> and </mfr>
def extract_mfr_data(sgml_content):
    pattern = re.compile(r'<mfr>(.*?)</mfr>', re.DOTALL)
    return pattern.findall(sgml_content)

# Prompt user for the file paths
input_path = input("Enter input file path: ").strip().strip('"')
output_path = input("Enter output file path (including the filename and .xlsx extension): ").strip().strip('"')

# Read the SGML file
with open(input_path, 'r', encoding='utf-8') as file:
    sgml_content = file.read()

# Extract the data
mfr_data = extract_mfr_data(sgml_content)

# Create a DataFrame
df = pd.DataFrame(mfr_data, columns=['MFR Data'])

# Write the data to an Excel file
df.to_excel(output_path, index=False)

print(f'Data has been successfully extracted to {output_path}')
