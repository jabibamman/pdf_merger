import glob
import os
import PyPDF2
import sys

def merge_pdfs(folder_path, output):
    if not output.endswith(".pdf"):
        print("Output file must end with .pdf")
        sys.exit(1)
    
    if os.path.exists(output):
        print("Output file already exists")
        sys.exit(1)

    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in glob.glob(os.path.join(folder_path, '*.pdf')):
        print(f"Adding {pdf_file}")
        pdf_merger.append(pdf_file)

    with open(output, 'wb') as fileobj:
        pdf_merger.write(fileobj)
        
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py \"output.pdf\" \"input_folder\"")
        sys.exit(1)

    output_path = sys.argv[1]
    input_folder = sys.argv[2]
    merge_pdfs(input_folder, output_path)
    print(f"Merged PDF files from {input_folder} into {output_path}")