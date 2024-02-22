import re
from .lexical_similarity import calcular_similitud_coseno

def extract_quotes(text):
    """
    Extrae comillas y citas de un texto.

    Esta función busca y extrae todas las comillas y citas presentes en el texto,
    incluyendo comillas simples, comillas dobles y paréntesis.

    Parámetros:
    - text (str): El texto del cual se extraerán las comillas y citas.

    Retorna:
    - list: Una lista de las comillas y citas encontradas en el texto.
    """
    pattern = r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\'|\(([^)]*)\)'
    matches = re.findall(pattern, text)    
    quotes = [match[0] for match in matches if match[0]] + [match[2] for match in matches if match[2]] + [match[4] for match in matches if match[4]]
    return quotes

def extract_cites(text):
    """
    Extrae las citas numeradas de un texto.

    Esta función busca y extrae todas las citas numeradas presentes en el texto.

    Parámetros:
    - text (str): El texto del cual se extraerán las citas.

    Retorna:
    - list: Una lista de las citas encontradas en el texto, ordenadas por su número.
    """
    pattern = r'\[(\d+)\]\s*([^\[]*)'
    matches = list(reversed(re.findall(pattern, text)))
    cite_dict = {}
    for num, cite in matches:
        if int(num) not in cite_dict:
            cite_dict[int(num)] = cite.strip()
   
    cites_list = list(cite_dict.values())
    return cites_list

def title_citation(titulo, citas):
    """
    Calcula la similitud coseno entre un título y una lista de citas.

    Esta función calcula la similitud coseno entre el título dado y cada una de las
    citas proporcionadas, retornando un diccionario con las citas como claves y la
    similitud coseno como valores.

    Parámetros:
    - titulo (str): El título contra el cual se compararán las citas.
    - citas (list): Una lista de citas para las cuales se calculará la similitud.

    Retorna:
    - dict: Un diccionario con las citas como claves y la similitud coseno como valores.
    """
    similitudes = {}
    for cita in citas:
        similitud = calcular_similitud_coseno(titulo, cita)
        similitudes[cita] = similitud
    return similitudes

def citation_check(doc1, doc1_title, doc2, doc2_title):
    """
    Compara las citas de dos documentos y retorna las referencias más similares.

    Esta función extrae las citas de dos documentos, compara cada cita con el título
    del otro documento, y retorna las citas que tienen una similitud coseno mayor o igual
    a  0.9, ordenadas por su similitud en orden descendente.

    Parámetros:
    - doc1 (str): El primer documento.
    - doc1_title (str): El título del primer documento.
    - doc2 (str): El segundo documento.
    - doc2_title (str): El título del segundo documento.

    Retorna:
    - tuple: Dos listas, la primera con las referencias del primer documento que
              tienen una similitud mayor o igual a  0.9 con el título del segundo
              documento, y la segunda con las referencias del segundo documento
              que tienen una similitud mayor o igual a  0.9 con el título del primer
              documento.
    """
    doc1_quotes = title_citation(doc2_title, extract_quotes(doc1) + list(extract_cites(doc1)))
    doc1_references = sorted([(cita, similitud) for cita, similitud in doc1_quotes.items() if similitud >=   0.8], key=lambda x: x[1], reverse=True)

    doc2_quotes = title_citation(doc1_title, extract_quotes(doc2) + list(extract_cites(doc2)))
    doc2_references = sorted([(cita, similitud) for cita, similitud in doc2_quotes.items() if similitud >=   0.8], key=lambda x: x[1], reverse=True)
    
    return doc1_references, doc2_references
