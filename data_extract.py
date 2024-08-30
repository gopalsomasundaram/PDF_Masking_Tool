from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as necessary


def ocr_image(image, language='eng'):
    try:
        if isinstance(image, str):
            # If image is a file path
            image = Image.open(image)
        elif isinstance(image, Image.Image):
            # If image is already a PIL Image object
            pass
        else:
            raise ValueError("Input must be a file path or a PIL Image object")

        text = pytesseract.image_to_string(image, lang=language)
        return text
    except Exception as e:
        print(f"Error during OCR: {e}")
        return ""