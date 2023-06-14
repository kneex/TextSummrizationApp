from PIL import Image


from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
#path_to_image = 'WWII wiki.png'

pytesseract.tesseract_cmd = path_to_tesseract

def extract(path_to_image):
    img = Image.open(path_to_image)

    text = pytesseract.image_to_string(img)

    return text
    
#extract(path_to_image)