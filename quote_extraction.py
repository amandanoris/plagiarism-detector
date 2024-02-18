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
    
    return cite_dict

def title_citation(titulo, citas):
    similitudes = []
    for i, cita in enumerate(citas):
        similitudes.append(calcular_similitud_coseno(titulo, cita))
    return similitudes

def citation_check(doc1, doc1_title, doc2, doc2_title):
   
    doc1_quotes = title_citation(doc2_title, extract_quotes(doc1) + list(extract_cites(doc1).values()))
    doc1_references = [i for i in doc1_quotes if i >=   0.9]  

    doc2_quotes = title_citation(doc1_title, extract_quotes(doc2) + list(extract_cites(doc2).values()))
    doc2_references = [i for i in doc2_quotes if i >=   0.9]  
    
    return doc1_references, doc2_references


doc1 = "el perro"
doc2 = "'el gato' y 'el perro'"
doc1_title = "el gato"
doc2_title = "dd"

doc1_references, doc2_references = citation_check(doc1, doc1_title, doc2, doc2_title)


if not doc1_references and not doc2_references:
    message = "Ningún documento referencia al otro."
elif doc1_references:
    message = f"El documento {doc1_title} referencia al otro en estas citas: {doc1_references}"
else:
  
    message = f"El documento {doc2_title} referencia al otro en estas citas: {doc2_references}"

print(message)