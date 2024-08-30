import fitz  # PyMuPDF
from PIL import Image
import io

def convert_pdf_to_image(pdf_path, dpi=300):
    images = []
    try:
        pdf_doc = fitz.open(pdf_path)
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc.load_page(page_num)
            zoom = dpi / 72.0
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
        return images
    except Exception as e:
        print(f"Error during PDF to image conversion: {e}")
        return []