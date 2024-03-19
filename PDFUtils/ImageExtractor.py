import fitz
import os
from glob import glob
import cv2
import numpy as np
import fitz

class ImageExtractor:
    def __init__(self, input_pdf_file):
        self.doc = fitz.open(input_pdf_file)
        self.tmp_filename = "tmp_img_"
        self.output_pdf = "converted.pdf"
        self.blank_pdf = "docs\\blankpage.pdf"

    def extract_images(self):
        for page_index in range(len(self.doc)):
            page = self.doc[page_index]
            image_list = page.get_images()

            if image_list:
                print(f"Found {len(image_list)} images on page {page_index}")
            else:
                print("No images found on page", page_index)

            for image_index, img in enumerate(image_list):
                xref = img[0]
                pix = fitz.Pixmap(self.doc, xref)

                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)

                pix.save(f"{self.tmp_filename}p_{page_index}_img_{image_index}.png")
                
    def delete_images(self):
        for img_file in glob(f"{self.tmp_filename}*.png"):
            os.remove(img_file)           
    

    def trim_border(self, image):
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Threshold the image to identify non-white regions
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        _, thresh = cv2.threshold(blurred, 253,255,cv2.THRESH_BINARY_INV)
                
        # Find contours of non-white regions
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Find the bounding box of the largest contour
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        
        # Crop the image using the bounding box
        cropped_image = image[y:y+h, x:x+w]
        
        return cropped_image

    def postprocess_images(self, display=False):
        for img_file in glob(f"{self.tmp_filename}*.png"):
            image = cv2.imread(img_file)                
            cropped_image = self.trim_border(image)
                        
            if (display):
                cv2.imshow('image', cropped_image)
                cv2.waitKey(0)
            
            cv2.imwrite(img_file, cropped_image)
            
    def insert_images(self, scale_factor=1.0):
        
        # Start position for the first image
        x, y = 150, 100

        doc = fitz.open(self.blank_pdf)
        page = doc[0]
        
        for img_file in glob(f"{self.tmp_filename}*.png"):              
            image = fitz.open(img_file)
            #width, height = image[0].rect.width, image[0].rect.height
            # Calculate the scaled width and height
            width = int(image[0].rect.width * scale_factor)
            height = int(image[0].rect.height * scale_factor)
            
            rect = fitz.Rect(x, y, x + width, y + height)
            page.insert_image(rect, filename=img_file)
            
            # Update y-coordinate for the next image
            y += height + 10  # Adjust the spacing between images as needed
        
        doc.save(self.output_pdf)
        doc.close()
            

# Example usage
if __name__ == "__main__":
    extractor = ImageExtractor("Aufenthaltstitel-ajithkrishnan.pdf")
    extractor.extract_images()
