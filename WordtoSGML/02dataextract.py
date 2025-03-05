import os
from docx import Document

def extract_all_data(docx_file):
    document = Document(docx_file)
    all_data = []
    
    nsmap = document.element.nsmap

    for element in document.element.body:
        if element.tag.endswith('p'):
            p_style = element.find('.//w:pStyle', nsmap)
            if p_style is not None and p_style.get('w:val') == 'ListParagraph':
                num_pr = element.find('.//w:numPr', nsmap)
                if num_pr is not None:
                    ilvl = num_pr.find('.//w:ilvl', nsmap)
                    if ilvl is not None:
                        list_type = 'Numbered List Item'
                        list_item = element.text.strip()
                        all_data.append(f"{list_type}: {list_item}")
                    else:
                        list_type = 'Bulleted List Item'
                        list_item = element.text.strip()
                        all_data.append(f"{list_type}: {list_item}")
            else:
                paragraph = element.text.strip()
                if paragraph:
                    all_data.append(f"Paragraph: {paragraph}")
        elif element.tag.endswith('tbl'):
            table_data = []
            for row in element:
                for cell in row:
                    if cell is not None and cell.text is not None:
                        table_data.append("Table Cell: " + cell.text.strip())
            all_data.append("Table:")
            all_data.extend(table_data)
        elif element.tag.endswith('pPr'):
            pass  # Skip paragraph properties
        else:
            all_data.append("Other Element: " + str(element))

    return "\n".join(all_data)

def main():
    folder_path = input("Enter the folder path containing the .docx file: ")

    # Verify if the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist:", folder_path)
        return

    # Get the list of .docx files in the folder
    docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]

    if not docx_files:
        print("No .docx files found in the folder:", folder_path)
        return

    for docx_file in docx_files:
        docx_file_path = os.path.join(folder_path, docx_file)
        output_file_path = os.path.splitext(docx_file_path)[0] + "_summary.txt"
        print("Processing file:", docx_file_path)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f"Summary for {docx_file}:\n")
            f.write(extract_all_data(docx_file_path))
            f.write("\n\n")

    print("All data summary has been saved in the input folder.")

if __name__ == "__main__":
    main()
