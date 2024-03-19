from ImageExtractor import ImageExtractor

if __name__ == '__main__':

    input_file = "Dutch_ResidencePermit_Belavadi.pdf"
    extractor = ImageExtractor(input_file)
    extractor.extract_images()
    extractor.postprocess_images()
    extractor.insert_images(0.3)
    #merge_id_card(input_file)