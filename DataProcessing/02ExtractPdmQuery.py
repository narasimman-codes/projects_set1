import os
import pandas as pd
from lxml import etree

def find_html_files(folder):
    html_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                html_files.append(file_path)
    return html_files

def extract_table_from_html(input_folder, output_folder):
    html_files = find_html_files(input_folder)
    for input_file_path in html_files:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()  # Read the HTML file as a string
            
            # Parse HTML content
            parser = etree.HTMLParser()
            tree = etree.fromstring(html_content, parser)
            
            # Find all tables in the HTML content
            tables = tree.xpath('//table')
            
            # Convert each table to DataFrame and save as Excel file
            for i, table in enumerate(tables):
                table_df = pd.read_html(etree.tostring(table))[0]
                output_file_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file_path))[0]}_{i}.xlsx")
                table_df.to_excel(output_file_path, index=False)
                print(f"Table extracted from {input_file_path} and saved as {output_file_path}")

if __name__ == "__main__":
    input_folder = input("Enter the folder path containing HTML files: ")
    if os.path.exists(input_folder):
        output_folder = input("Enter the output folder path: ")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        extract_table_from_html(input_folder, output_folder)
    else:
        print("Folder does not exist.")
