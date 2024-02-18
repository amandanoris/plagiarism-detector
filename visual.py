from flask import Flask, request, jsonify, render_template
from Procesamiento import PlagiarismDetector
from Procesamiento import TextPreprocessor
from lexical_similarity import calcular_similitud_coseno
from semantic_similarity import calcular_similitud_semantica
from quote_extraction import citation_check
from pathlib import Path

app = Flask(__name__)

preprocessor = TextPreprocessor()
detector = PlagiarismDetector(preprocessor)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        doc1 = request.files.get('doc1')
        doc2 = request.files.get('doc2')
        
        if not doc1 or not doc2:
            return jsonify({'error': 'Faltan los documentos para comparar'}),   
   
        if doc1.filename == '' or doc2.filename == '':
            return jsonify({'error': 'No se seleccionó ningún archivo'}),   
        
        doc1_content = doc1.read().decode('utf-8')
        doc2_content = doc2.read().decode('utf-8')

        doc1_name=Path(doc1.filename).stem
        doc2_name=Path(doc2.filename).stem

        lexical_similarity = calcular_similitud_coseno(doc1_content, doc2_content)
        semantic_similarity = calcular_similitud_semantica(doc1_content, doc2_content)
        plagiarism_segments = detector.detect_plagiarism(doc1_content, doc2_content)
        doc1_references, doc2_references = citation_check(doc1_content, doc1_name, doc2_content, doc2_name)
        
        return render_template('index.html', plagiarism_segments=plagiarism_segments, lexical_similarity=lexical_similarity, semantic_similarity = semantic_similarity, doc1_references=doc1_references, doc2_references=doc2_references, doc1_name=doc1_name, doc2_name=doc2_name)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
