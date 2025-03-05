from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import os
import time
from selenium import webdriver

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Extract details based on CAGE codes.")
parser.add_argument("input_file", help="Path to the input Excel file")
args = parser.parse_args()

input_file = args.input_file

# Validate input file
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

output_dir = os.path.dirname(input_file)
output_file = os.path.join(output_dir, "output_data.xlsx")

# ChromeDriver setup (update driver path)
driver_path = r"C:\Users\nkaliyap\AppData\Local\SeleniumBasic\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Read input Excel file
data = pd.read_excel(input_file)
data['CAGE Code'] = data['CAGE Code'].astype(str)  # Ensure codes are strings

results = []

try:
    for cage_code in data['CAGE Code']:
        # Navigate to the target page
        driver.get("http://crus02v1.rockwellcollins.com:7001/srm63/RCcustom/rcutils/supplierCAGEDialog.jsp")

        # Wait for the input field
        wait = WebDriverWait(driver, 10)
        cage_input = wait.until(EC.presence_of_element_located((By.NAME, "supplierCAGENumber")))

        # Clear and enter CAGE code
        cage_input.clear()
        cage_input.send_keys(cage_code[:5])  # Ensure it's only 5 characters
        cage_input.send_keys(Keys.RETURN)

        # Wait for the result page to load (adjust as needed)
        time.sleep(5)

        # Get the page source
        page_source = driver.page_source

        # Print the page source to debug (only print part of it)
        print("Page Source after search:")
        print(page_source[:1000])  # Print only the first 1000 characters for inspection

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Define the labels to search for
        labels = [
            "Name", "Division", "Phone", "Address1", "Address2", "City", "State", "Zip Code", "Country"
        ]

        extracted_data = {}
        
        # Search for each label and extract the corresponding data
        for label in labels:
            # Print out the search label for debugging
            print(f"Searching for {label}")

            # Search for the label in the page
            row = soup.find('td', text=lambda x: x and label in x)  # Flexible search for label
            if row:
                # Find the next <td> containing the value (in the same <tr>)
                value = row.find_next('td')
                if value:
                    extracted_data[label] = value.get_text(strip=True)
                    print(f"Found {label}: {value.get_text(strip=True)}")
                else:
                    extracted_data[label] = "Not Found"
            else:
                extracted_data[label] = "Not Found"
                print(f"{label} Not Found")

        results.append(extracted_data)

finally:
    driver.quit()

# Save results to Excel
output_df = pd.DataFrame(results)
final_output = pd.concat([data, output_df], axis=1)
final_output.to_excel(output_file, index=False)
print(f"Extracted data saved to '{output_file}'.")
