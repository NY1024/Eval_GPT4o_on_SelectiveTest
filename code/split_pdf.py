import fitz  # PyMuPDF
from PIL import Image

# Open the PDF file
pdf_path = './2021/Practice-test-2021-Thinking-questions.pdf'
pdf_document = fitz.open(pdf_path)

# Iterate through each page of the PDF
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)  # Load the page
    pix = page.get_pixmap()  # Get the page's pixmap
    
    # Convert the pixmap to an Image object
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Save as a PNG file
    img.save(f'page_{page_num + 1}.png', 'PNG')

print("PDF pages have been successfully converted to PNG format")
