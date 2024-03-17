import PyPDF2
import sys

def get_page_dimensions(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        page = reader.pages[0]
        width = page.mediabox.width
        height = page.mediabox.height
    return width, height

def scale_page(page, width, height, target_width, target_height):
    scaling_factor_x = round(target_width / width,2)
    scaling_factor_y = round(target_height / height, 2)
    
    #page.scale_to(scaling_factor_x, scaling_factor_y)
    page.scale_by(scaling_factor_x)
    return page

def merge_pdfs(pdf_files, output_filename):
    writer = PyPDF2.PdfWriter()
    
    # Get dimensions of the first PDF
    first_pdf_width, first_pdf_height = get_page_dimensions(pdf_files[0])

    for pdf in pdf_files:
        with open(pdf, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                # Scale the page to match dimensions of the first PDF
                page = scale_page(page, *get_page_dimensions(pdf), first_pdf_width, first_pdf_height)
                writer.add_page(page)
    
    with open(output_filename, 'wb') as f:
        writer.write(f)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please enter the path to PDF files!")
        exit(1)
    else:
        pdf_files = []
        for i in range(1, len(sys.argv)):
            pdf_files.append(sys.argv[i])
            
        #for p in pdf_files:
        #    print(p)
        output_filename = "merged.pdf"
        merge_pdfs(pdf_files, output_filename)
