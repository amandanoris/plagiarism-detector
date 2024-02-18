import re
from lexical_similarity import calcular_similitud_coseno

def extract_quotes(text):
    pattern = r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\'|\(([^)]*)\)'
    matches = re.findall(pattern, text)    
    quotes = [match[0] for match in matches if match[0]] + [match[2] for match in matches if match[2]] + [match[4] for match in matches if match[4]]
    return quotes

def extract_cites(text):
    pattern = r'\[(\d+)\]\s*([^\[]*)'
    matches = list(reversed(re.findall(pattern, text)))
    cite_dict = {}
    for num, cite in matches:
        if int(num) not in cite_dict:
            cite_dict[int(num)] = cite.strip()
    # Convertir los valores del diccionario a una lista
    cites_list = list(cite_dict.values())
    return cites_list

def title_citation(titulo, citas):
    similitudes = {}
    for cita in citas:
        similitud = calcular_similitud_coseno(titulo, cita)
        similitudes[cita] = similitud
    return similitudes

def citation_check(doc1, doc1_title, doc2, doc2_title):
    doc1_quotes = title_citation(doc2_title, extract_quotes(doc1) + list(extract_cites(doc1)))
    doc1_references = sorted([(cita, similitud) for cita, similitud in doc1_quotes.items() if similitud >=  0.9], key=lambda x: x[1], reverse=True)

    doc2_quotes = title_citation(doc1_title, extract_quotes(doc2) + list(extract_cites(doc2)))
    doc2_references = sorted([(cita, similitud) for cita, similitud in doc2_quotes.items() if similitud >=  0.9], key=lambda x: x[1], reverse=True)
    
    return doc1_references, doc2_references

doc1 = "el perro come [3] huesos  [3] dd"
doc2 = "'la vida de los gatos' y 'el perro'"
doc1_title = "la vida de los gatos"
doc2_title = "dd"

doc1_references, doc2_references = citation_check(doc1, doc1_title, doc2, doc2_title)

if doc1_references and not doc2_references:
    message = f"El documento {doc1_title} referencia al otro en estas citas: {doc1_references}"
elif doc1_references and doc2_references:
    message = f"El documento {doc1_title} referencia al otro en estas citas: {doc1_references} y el documento {doc2_title} referencia al otro en estas citas: {doc2_references}"
else:
    message = "Ningún documento referencia al otro."

print(message)