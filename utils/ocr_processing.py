import pytesseract
import cv2
from pdf2image import convert_from_path
import os
from utils.pdf_creation import create_pdf
from PIL import Image
import numpy as np

# Set the Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_document(file_path, original_filename):
    # Convert PDF to images if needed
    if file_path.lower().endswith('.pdf'):
        pages = convert_from_path(file_path)
    else:
        pages = [Image.open(file_path)]
    
    text_content = []
    for page in pages:
        img = np.array(page)
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, thresh_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        # Extract text
        text = pytesseract.image_to_string(thresh_img)
        text_content.append(text)
    
    # Create a clear PDF with recognized text
    output_filename = os.path.splitext(original_filename)[0] + '_processed.pdf'
    output_path = os.path.join('outputs', output_filename)
    create_pdf(text_content, output_path)
    return output_path
