import os
from docx import Document

def extract_paragraphs_from_docx(docx_file):
    """
    Extract paragraphs and their content from a .docx file.
    """
    doc = Document(docx_file)
    paragraphs = {}
    heading_counts = {}
    paragraph_counts = {}
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():  # Ignore empty paragraphs
            # Determine the heading level
            if paragraph.style.name.startswith('Heading'):
                heading_level = int(paragraph.style.name.split(' ')[-1])
                heading_counts[heading_level] = heading_counts.get(heading_level, 0) + 1
                variable_name = f"heading_{heading_level}_{heading_counts[heading_level]}"
            else:
                paragraph_counts[0] = paragraph_counts.get(0, 0) + 1
                variable_name = f"paragraph_{paragraph_counts[0]}"
            paragraphs[variable_name] = paragraph.text
    return paragraphs

def main():
    # Prompt the user to input the folder path
    folder_path = input("Enter the folder path containing .docx files: ")

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder not found.")
        return

    # Extract all .docx files in the folder
    docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]

    # Process each .docx file
    for docx_file in docx_files:
        docx_path = os.path.join(folder_path, docx_file)
        # Extract paragraphs from the .docx file
        paragraphs = extract_paragraphs_from_docx(docx_path)
        
        # Write the paragraphs to a .txt file
        output_filename = os.path.splitext(docx_file)[0] + '_output.txt'
        output_path = os.path.join(folder_path, output_filename)
        with open(output_path, 'w') as txt_file:
            for variable_name, paragraph_text in paragraphs.items():
                txt_file.write(f"{variable_name}: {paragraph_text}\n")
        print(f"Processed: {docx_file}. Output saved to: {output_path}")

if __name__ == "__main__":
    main()
