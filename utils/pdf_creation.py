from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(text_content, output_filename):
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    
    for page_text in text_content:
        text = c.beginText(40, height - 40)
        text.setFont("Helvetica", 12)
        text.setLeading(14)
        text.textLines(page_text)
        c.drawText(text)
        c.showPage()
    
    c.save()
