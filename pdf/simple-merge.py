import PyPDF2
import sys

def merge_pdfs(pdf_files, output_filename):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please enter the path to PDF files!")
        exit(1)
    else:
        pdf_files = []
        for i in range(1, len(sys.argv)):
            pdf_files.append(sys.argv[i])
            
        for p in pdf_files:
            print(p)
        output_filename = "merged.pdf"
        merge_pdfs(pdf_files, output_filename)
       