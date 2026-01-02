import pdfplumber
from docx import Document
import io

async def extract_text(file_content: bytes, extension: str) -> str:
    text = ""
    if extension == ".pdf":
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif extension in [".docx", ".doc"]:
        doc = Document(io.BytesIO(file_content))
        text = "\n".join(para.text for para in doc.paragraphs)
    return text.strip()
