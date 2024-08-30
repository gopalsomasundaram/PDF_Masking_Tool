# PDF Masking Tool

The PDF Masking Tool is a Python application that allows users to automatically detect and mask sensitive information in PDF documents. It uses OCR (Optical Character Recognition) to extract text from PDFs, analyzes the content for sensitive information, and then masks the identified sensitive data in the output PDF.

## Features

- User-friendly graphical interface
- PDF to image conversion
- OCR text extraction
- Automatic detection of sensitive information
- PDF masking
- Progress tracking

## Requirements

- Python 3.7+
- Tesseract OCR engine
- PyMuPDF (fitz)
- Pillow (PIL)
- pytesseract
- tkinter

## Installation

1. Clone this repository
2. Install the required Python packages: `pip install -r requirements.txt`
3. Install Tesseract OCR:
- For Windows: Download and install from [GitHub Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- For macOS: `brew install tesseract`
- For Linux: `sudo apt-get install tesseract-ocr`

4. Update the Tesseract path in `data_extract.py` if necessary.

## Usage

Run the main script:
1. Click "Browse" to select an input PDF file.
2. The output file path will be automatically generated. You can change it if desired.
3. Click "Mask PDF" to start the process.
4. The progress bar will show the current status of the operation.
5. Once complete, a success message will appear, and the masked PDF will be saved.

## How It Works

1. The input PDF is converted to images.
2. OCR is performed on these images to extract text.
3. The extracted text is analyzed to identify sensitive information.
4. The original PDF is then masked based on the identified sensitive data.
5. A new, masked PDF is saved to the specified output location.

## Files

- `main.py`: The main script that orchestrates the entire process.
- `tkin.py`: Contains the GUI implementation using tkinter.
- `pdf_to_img.py`: Handles PDF to image conversion.
- `data_extract.py`: Performs OCR on images.
- `masking.py`: Applies masking to the PDF.
- `gemini_api.py`: Integrates with an API for text analysis (not provided in the shared code).

## Notes

- Ensure that you have the necessary permissions to read the input PDF and write to the output location.
- The accuracy of sensitive information detection depends on the OCR quality and the analysis algorithm.
- Large PDF files may take longer to process.

## Developers

- Gopal Somasundaram(https://github.com/gopalsomasundaram)
- Dhruv Desai(https://github.com/dhruvdesai09)
