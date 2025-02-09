import fitz  # PyMuPDF

def extract_text(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text
