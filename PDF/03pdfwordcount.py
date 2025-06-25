import os
import re
import pandas as pd
from PyPDF2 import PdfReader

def count_words(text):
    # Basic word tokenizer
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def get_pdf_word_counts(directory):
    results = []

    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            try:
                reader = PdfReader(file_path)
                full_text = ""
                for page in reader.pages:
                    full_text += page.extract_text() or ""
                word_count = count_words(full_text)
                results.append({
                    "Filename": filename,
                    "Word Count": word_count
                })
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                results.append({
                    "Filename": filename,
                    "Word Count": "Error"
                })
    return results

if __name__ == "__main__":
    input_dir = input("Enter the full path of the directory with PDF files: ").strip('"')

    if not os.path.isdir(input_dir):
        print("Invalid directory path. Please double-check.")
    else:
        data = get_pdf_word_counts(input_dir)
        df = pd.DataFrame(data)
        output_path = os.path.join(input_dir, "pdf_word_counts.xlsx")
        df.to_excel(output_path, index=False)
        print(f"\n✅ Word counts exported to: {output_path}")
