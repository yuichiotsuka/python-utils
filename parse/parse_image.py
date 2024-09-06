import pytesseract
from PIL import Image


def read_image(image_src, tesseract_src=None):
    """Reads an image into text using PyTesseract.

    Uses PyTesseract and PIL modules to parse a file,
    and returns a string.

    Typical usage example:
      
      text_1 = read_image(image_src='image.png')
      text_2 = read_image(image_src='image.png', tesseract_src='C:/Progs/Tesseract-OCR')
    """

    # open the image
    image_instance = Image.open(image_src)
    
    # OCR using PyTesseract
    parsed_text = pytesseract.image_to_string(image_instance)

    return parsed_text

def main():
    print("Hello World!")

    text_1 = read_image(image_src='C:/temp/sampletext-660x75.png', tesseract_src='C:/Progs/Tesseract-OCR')
    text_2 = read_image(image_src='C:/temp/Image.png')

    print(text_1)
    print(text_2)

if __name__ == "__main__":
    main()