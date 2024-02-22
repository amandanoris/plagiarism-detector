from docx import Document
from PyPDF2 import PdfReader
from pathlib import Path

def read_docx(file):
    """
    Lee un archivo .docx y devuelve su contenido como una cadena de texto.

    Utiliza la biblioteca 'docx' para abrir el archivo y extraer el texto de cada párrafo.

    Parámetros:
    - file (str): La ruta al archivo .docx.

    Retorna:
    - str: El contenido del archivo .docx como una cadena de texto.
    """
    doc = Document(file)
    return ' '.join([paragraph.text for paragraph in doc.paragraphs])

def read_pdf(file):
    """
    Lee un archivo .pdf y devuelve su contenido como una cadena de texto.

    Utiliza la biblioteca 'PyPDF2' para abrir el archivo y extraer el texto de cada página.

    Parámetros:
    - file (str): La ruta al archivo .pdf.

    Retorna:
    - str: El contenido del archivo .pdf como una cadena de texto.
    """
    pdf_file_obj = file.stream
    pdf_reader = PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    return text

def read_file(file):
    """
    Determina el tipo de archivo por su extensión y lee su contenido.

    Soporta archivos .txt, .docx y .pdf. Si el archivo es de otro tipo, se lanza una excepción.

    Parámetros:
    - file (str): La ruta al archivo a leer.

    Retorna:
    - str: El contenido del archivo como una cadena de texto.

    Raises:
    - ValueError: Si el formato del archivo no es soportado.
    """
    extension = Path(file.filename).suffix
    if extension == '.txt':
        return file.read().decode('utf-8')
    elif extension == '.docx':
        return read_docx(file)
    elif extension == '.pdf':
        return read_pdf(file)
    else:
        raise ValueError(f'Formato de archivo no soportado: {extension}')
