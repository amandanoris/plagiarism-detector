from docx import Document
from PyPDF2 import PdfReader
from pathlib import Path


def read_docx(file):
    doc = Document(file)
    return ' '.join([paragraph.text for paragraph in doc.paragraphs])

def read_pdf(file):
    pdf_file_obj = file.stream
    pdf_reader = PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    return text



def read_file(file):
    extension = Path(file.filename).suffix
    if extension == '.txt':
        return file.read().decode('utf-8')
    elif extension == '.docx':
        return read_docx(file)
    elif extension == '.pdf':
        return read_pdf(file)
    else:
        raise ValueError(f'Formato de archivo no soportado: {extension}')
