import PyPDF2
import sys

class PDFMerger:
    def __init__(self, pdf_files):
        self.pdf_files = pdf_files
        self.output_filename = "merged.pdf"

    def get_page_dimensions(self, pdf_path):
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            page = reader.pages[0]
            width = page.mediabox.width
            height = page.mediabox.height
        return width, height

    def scale_page(self, page, width, height, target_width, target_height):
        scaling_factor_x = round(target_width / width, 2)
        scaling_factor_y = round(target_height / height, 2)
        
        # page.scale_to(scaling_factor_x, scaling_factor_y)
        page.scale_by(scaling_factor_x)
        return page

    def merge_pdfs(self):
        writer = PyPDF2.PdfWriter()
        
        # Get dimensions of the first PDF
        first_pdf_width, first_pdf_height = self.get_page_dimensions(self.pdf_files[0])

        for pdf in self.pdf_files:
            with open(pdf, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    # Scale the page to match dimensions of the first PDF
                    page = self.scale_page(page, *self.get_page_dimensions(pdf), first_pdf_width, first_pdf_height)
                    writer.add_page(page)
        
        with open(self.output_filename, 'wb') as f:
            writer.write(f)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter the path to PDF files!")
        sys.exit(1)
    else:
        pdf_files = sys.argv[1:]
        merger = PDFMerger(pdf_files)
        merger.merge_pdfs()
