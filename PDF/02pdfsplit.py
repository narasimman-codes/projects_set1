import os
import fitz  # PyMuPDF

def get_unique_filename(base_path, extension):
    """
    Generate a unique filename by appending a counter if the file already exists.
    """
    counter = 1
    unique_path = f"{base_path}{extension}"
    while os.path.exists(unique_path):
        unique_path = f"{base_path} ({counter}){extension}"
        counter += 1
    return unique_path

def split_pdf(input_pdf_path, output_folder):
    """
    Splits all PDF files (case-insensitive) found in the input directory and its subdirectories into individual pages.
    Each page is saved as a separate PDF in the corresponding output directory.
    """
    for root, dirs, files in os.walk(input_pdf_path):
        for file in files:
            if file.lower().endswith('.pdf'):  # Case-insensitive check for '.pdf'
                try:
                    input_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(root, input_pdf_path)
                    output_file_dir = os.path.join(output_folder, relative_path)
                    output_file_path_base = os.path.join(output_file_dir, os.path.splitext(file)[0])

                    os.makedirs(output_file_dir, exist_ok=True)

                    pdf_document = fitz.open(input_file_path)
                    print(f"Processing file: {file} ({pdf_document.page_count} pages)")

                    for page_num in range(pdf_document.page_count):
                        # Generate a unique filename to avoid overwriting
                        base_path = f"{output_file_path_base} - Page {page_num + 1}"
                        output_pdf_path = get_unique_filename(base_path, ".pdf")
                        
                        pdf_writer = fitz.open()
                        pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
                        pdf_writer.save(output_pdf_path)
                        pdf_writer.close()

                        print(f'  Extracted Page {page_num + 1} of "{file}" to "{output_pdf_path}".')

                    pdf_document.close()
                    print(f"Finished processing: {file}")

                except Exception as e:
                    print(f"Error processing file {file}: {e}")

if __name__ == "__main__":
    input_path = input("Enter input directory path: ").strip()
    output_path = input("Enter output directory path: ").strip()

    # Validate paths
    if not os.path.isdir(input_path):
        print("Invalid input directory path. Please enter a valid directory.")
    else:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Output directory created: {output_path}")

        print(f"Processing PDF files in: {input_path}")
        split_pdf(input_path, output_path)
        print("Processing complete.")
