from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import sys, os

def compress(fname:str):
        
    merger = PdfWriter()    
    writer = PdfWriter()
   
    for pdf in [fname]:
        merger.append(pdf)
        
    for page in merger.pages:
        page.compress_content_streams()  # This is CPU intensive! (lossless compression)
        writer.add_page(page)
 
    with open(fname, "wb") as f:
        writer.write(f)
    
    print("Saved ", fname)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please enter the path to PDF file!")
        exit(1)
    else:
        for i in range(1, len(sys.argv)):
            compress(sys.argv[i])
        
       