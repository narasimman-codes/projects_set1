import os
import fitz  # PyMuPDF

def split_pdf(input_pdf_path, output_folder):
    for root, dirs, files in os.walk(input_pdf_path):
        for file in files:
            if file.endswith('.pdf'):
                input_file_path = os.path.join(root, file)
                output_file_dir = os.path.join(output_folder, os.path.relpath(root, input_pdf_path))
                output_file_path_base = os.path.join(output_file_dir, os.path.splitext(file)[0])

                if not os.path.exists(output_file_dir):
                    os.makedirs(output_file_dir)

                pdf_document = fitz.open(input_file_path)
                for page_num in range(pdf_document.page_count):
                    page = pdf_document[page_num]
                    output_pdf_path = f"{output_file_path_base} {page_num + 1}.pdf"
                    pdf_writer = fitz.open()
                    pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
                    pdf_writer.save(output_pdf_path)
                    pdf_writer.close()

                    print(f'Page {page_num + 1} of {file} extracted successfully.')

                pdf_document.close()

# Example usage
input_path = input("Enter input directory path: ")
output_path = input("Enter output directory path: ")

split_pdf(input_path, output_path)
