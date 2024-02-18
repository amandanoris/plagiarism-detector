from flask import Flask, request, jsonify, render_template
from Procesamiento import PlagiarismDetector
from Procesamiento import TextPreprocessor
from lexical_similarity import calcular_similitud_coseno
from semantic_similarity import calcular_similitud_semantica

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

        lexical_similarity = calcular_similitud_coseno(doc1_content, doc2_content)
        semantic_similarity = calcular_similitud_semantica(doc1_content, doc2_content)
        plagiarism_segments = detector.detect_plagiarism(doc1_content, doc2_content)
        
        return render_template('index.html', plagiarism_segments=plagiarism_segments, lexical_similarity=lexical_similarity, semantic_similarity = semantic_similarity)
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
