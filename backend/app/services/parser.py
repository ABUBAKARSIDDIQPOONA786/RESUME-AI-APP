import pdfplumber
from docx import Document
from io import BytesIO

def extract_text(file):
    content = file.file.read()
    
    if file.filename.endswith(".pdf"):
        return extract_pdf(content)
    elif file.filename.endswith(".docx"):
        return extract_docx(content)
    else:
        return ""

def extract_pdf(content):
    text = ""
    with pdfplumber.open(BytesIO(content)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def extract_docx(content):
    doc = Document(BytesIO(content))
    return "\n".join([p.text for p in doc.paragraphs]).strip()