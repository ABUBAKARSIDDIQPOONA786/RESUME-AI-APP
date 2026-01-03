import io
from PyPDF2 import PdfReader
import docx

def parse_resume(file):
    content = file.file.read()
    filename = file.filename.lower()

    try:
        if filename.endswith(".pdf"):
            reader = PdfReader(io.BytesIO(content))
            return "\n".join(
                page.extract_text() or "" for page in reader.pages
            )

        elif filename.endswith(".docx"):
            doc = docx.Document(io.BytesIO(content))
            return "\n".join(p.text for p in doc.paragraphs)

        else:
            raise ValueError("Unsupported file format")

    except Exception as e:
        print("❌ Parsing error:", e)
        return ""
