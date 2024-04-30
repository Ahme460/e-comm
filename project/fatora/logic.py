import pytesseract
from PIL import Image

def conver(image):

    # Open the image file
    image = Image.open('image.png')

    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)



