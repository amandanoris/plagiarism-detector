from flask import Blueprint, request, jsonify, render_template
from pathlib import Path

app = Blueprint('gui', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Maneja las solicitudes GET y POST para la página principal de la aplicación.

    En caso de una solicitud POST, procesa dos documentos enviados por el usuario,
    calcula la similitud léxica y semántica entre ellos, detecta plagio y verifica
    las citas, y luego muestra los resultados en la página principal.

    En caso de una solicitud GET, simplemente renderiza la página principal sin contenido.

    Retorna:
    - render_template: Un template HTML renderizado con los resultados de la comparación
      si la solicitud es POST, o simplemente la página principal sin contenido si es GET.
    """
    preprocessor = app.preprocessor
    detector = app.detector
    calcular_similitud_coseno = app.calcular_similitud_coseno
    calcular_similitud_semantica = app.calcular_similitud_semantica
    citation_check = app.citation_check
    read_file = app.read_file
    show = app.show

    if request.method == 'POST':
        doc1 = request.files.get('doc1')
        doc2 = request.files.get('doc2')
        
        if not doc1 or not doc2:
            return jsonify({'error': 'Faltan los documentos para comparar'}),
       
        if doc1.filename == '' or doc2.filename == '':
            return jsonify({'error': 'No se seleccionó ningún archivo'}),
        
        doc1_content = read_file(doc1)
        doc2_content = read_file(doc2)

        doc1_name=Path(doc1.filename).stem
        doc2_name=Path(doc2.filename).stem

        preprocessed_doc1 = preprocessor.preprocess(doc1_content)
        preprocessed_doc2 = preprocessor.preprocess(doc2_content)

        show(doc1_content, doc1_name)
        show(doc2_content, doc2_name)

        lexical_similarity = calcular_similitud_coseno(doc1_content, doc2_content)
        semantic_similarity = calcular_similitud_semantica(preprocessed_doc1, preprocessed_doc2)
        plagiarism_segments = detector.detect_plagiarism(doc1_content, doc2_content)
        doc1_references, doc2_references = citation_check(doc1_content, doc1_name, doc2_content, doc2_name)
        
        return render_template('index.html', has_contents = True, plagiarism_segments=plagiarism_segments, lexical_similarity=lexical_similarity, semantic_similarity=semantic_similarity, doc1_references=doc1_references, doc2_references=doc2_references, doc1_name=doc1_name, doc2_name=doc2_name)
    else:
        return render_template('index.html', has_contents = False)
