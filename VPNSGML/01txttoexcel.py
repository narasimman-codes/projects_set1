import re
import pandas as pd

# Prompt the user for input and output file paths
input_path = input("Enter input file path: ").strip().strip('"')
output_path = input("Enter output file path: ").strip().strip('"')

# Verify the output file extension
if not output_path.lower().endswith('.xlsx'):
    print("Error: Output file must have a .xlsx extension")
    exit(1)

# Read the SGML file
try:
    with open(input_path, 'r') as file:
        sgml_content = file.read()
except OSError as e:
    print(f"Error opening file: {e}")
    exit(1)

# Define regex patterns to extract data
itemdata_pattern = re.compile(r'<itemdata(.*?)</itemdata>', re.DOTALL)
pnr_pattern = re.compile(r'<pnr>(.*?)</pnr>')
pspmfr_pattern = re.compile(r'<pspmfr>(.*?)</pspmfr>')
optmfr_pattern = re.compile(r'<optmfr>(.*?)</optmfr>')

# Extract itemdata sections
itemdata_sections = itemdata_pattern.findall(sgml_content)

# Parse each itemdata section
parsed_data = []
for section in itemdata_sections:
    item = {}
    pnr_match = pnr_pattern.search(section)
    pspmfr_match = pspmfr_pattern.search(section)
    optmfr_matches = optmfr_pattern.findall(section)
    
    item['pnr'] = pnr_match.group(1) if pnr_match else None
    item['pspmfr'] = pspmfr_match.group(1) if pspmfr_match else None
    
    # Handling multiple <optmfr> tags by joining them with a comma
    item['optmfr'] = ', '.join(optmfr_matches) if optmfr_matches else None
    
    parsed_data.append(item)

# Convert to DataFrame
df = pd.DataFrame(parsed_data)

# Save to Excel
try:
    df.to_excel(output_path, index=False)
    print(f"Data has been successfully converted and saved to {output_path}")
except Exception as e:
    print(f"Error saving to Excel: {e}")
    exit(1)
