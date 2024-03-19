import fitz

input_file = "Aufenthaltstitel-ajithkrishnan.pdf"
output_file = "example-with-barcode.pdf"
barcode_file = "021.png"

# define the position (upper-right corner)
image_rectangle = fitz.Rect(450,20,550,120)

# retrieve the first page of the PDF
file_handle = fitz.open(input_file)
first_page = file_handle[0]

# add the image
first_page.insert_image(fitz.Rect(0,0,50,50),filename=barcode_file)

file_handle.save(output_file)