from pdf_to_img import convert_pdf_to_image
from data_extract import ocr_image
from gemini_api import mask_text
from masking import mask_text_in_pdf
from tkin import run_gui

def process_pdf(pdf_path, output_pdf_path, progress_callback=None, language='eng'):
    dpi = 300
    ocr_text = ""

    # Convert PDF to images
    images = convert_pdf_to_image(pdf_path, dpi)

    if not images:
        raise Exception("Failed to convert PDF to images")

    total_steps = len(images) + 2  # OCR + masking + saving
    current_step = 0

    for img in images:
        # Perform OCR on each image
        ocr_text += ocr_image(img, language)
        current_step += 1
        if progress_callback:
            progress_callback(current_step / total_steps * 100)

    sensitive_info_response = mask_text(ocr_text)
    current_step += 1
    if progress_callback:
        progress_callback(current_step / total_steps * 100)

    if sensitive_info_response:
        text_to_change = sensitive_info_response.text
        target_texts = text_to_change.split(',')
        mask_text_in_pdf(pdf_path, output_pdf_path, target_texts)

    if progress_callback:
        progress_callback(100)  # Task complete

if __name__ == "__main__":
    run_gui(process_pdf)