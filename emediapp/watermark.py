from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_watermark(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 20)
    c.setFillGray(0.5, 0.5)  
    c.drawString(100, 500, "EMEDI - Confidential")
    c.drawString(100, 480, "Date: 05/12/2024")
    c.save()

create_watermark("watermark.pdf")