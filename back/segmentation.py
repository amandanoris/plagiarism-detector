import spacy
from transformers import BertModel, BertTokenizer
import torch
from sklearn.metrics.pairwise import cosine_similarity
from .lexical_similarity import calcular_similitud_coseno

class SemanticVectorizer:
    """
    Clase para vectorizar texto usando el modelo BERT preentrenado.

    Esta clase utiliza el tokenizador y el modelo BERT de la biblioteca transformers para
    convertir texto en vectores semánticos. Estos vectores se utilizan para comparar
    la similitud semántica entre diferentes segmentos de texto.
    """

    def __init__(self):
        """
        Inicializa el tokenizador y el modelo BERT.

        Se carga el modelo BERT 'bert-base-uncased' preentrenado y su tokenizador correspondiente.
        """
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def vectorize(self, text):
        """
        Vectoriza un segmento de texto utilizando BERT.

        Este método toma un segmento de texto como entrada, lo tokeniza y lo pasa a través del modelo BERT
        para obtener un vector semántico. El vector resultante es el promedio de los estados ocultos del último
        token en el texto.

        Parámetros:
        - text (str): El texto a vectorizar.

        Retorna:
        - numpy.ndarray: Un vector semántico del texto de entrada.
        """
        input_ids = self.tokenizer.encode(text, add_special_tokens=True)
        input_ids = torch.tensor([input_ids])
        with torch.no_grad():
            last_hidden_states = self.model(input_ids)[0]
        return last_hidden_states[0].mean(dim=0).numpy()

class PlagiarismDetector:
    """
    Clase para detectar plagio entre dos documentos utilizando vectores semánticos.

    Esta clase utiliza la clase SemanticVectorizer para convertir segmentos de texto en vectores semánticos
    y luego compara estos vectores para detectar similitudes que pueden indicar plagio.
    """

    def __init__(self, preprocessor):
        """
        Inicializa el detector de plagio con un preprocesador y un vectorizador semántico.

        Parámetros:
        - preprocessor (Preprocessor): Un objeto que puede preprocesar texto para mejorar la precisión de la detección de plagio.
        """
        self.preprocessor = preprocessor
        self.tokenizer = SemanticVectorizer()
        self.nlp = spacy.load('en_core_web_sm')

    def segment_text(self, text):
        """
        Divide un documento en segmentos de texto.

        Este método utiliza spaCy para dividir el texto en párrafos y luego en oraciones.
        Cada segmento se representa como una tupla que contiene el texto de la oración y sus índices de inicio y fin.

        Parámetros:
        - text (str): El texto del documento a segmentar.

        Retorna:
        - list: Una lista de tuplas, cada una representando una oración del documento.
        """
        doc = self.nlp(text)
        paragraphs = [(sent.text, sent.start, sent.end) for sent in doc.sents]
        return paragraphs

    def detect_plagiarism(self, doc1, doc2, threshold=0.85):
        """
        Detecta plagio entre dos documentos comparando sus segmentos.

        Este método divide los documentos en segmentos, los preprocesa y vectoriza, y luego compara
        las similitudes semánticas entre los segmentos. Los segmentos con una similitud mayor al umbral
        especificado se consideran plagiados.

        Parámetros:
        - doc1 (str): El primer documento a comparar.
        - doc2 (str): El segundo documento a comparar.
        - threshold (float, opcional): El umbral de similitud para considerar un segmento como plagiado.

        Retorna:
        - list: Una lista de tuplas, cada una representando un segmento plagiado junto con su similitud.
        """
        segments_doc1 = self.segment_text(doc1)
        segments_doc2 = self.segment_text(doc2)

        preprocessed_segments_doc1 = [self.preprocessor.preprocess(segment[0]) for segment in segments_doc1]
        preprocessed_segments_doc2 = [self.preprocessor.preprocess(segment[0]) for segment in segments_doc2]

        vectorized_doc1 = [self.tokenizer.vectorize(segment) for segment in preprocessed_segments_doc1]
        vectorized_doc2 = [self.tokenizer.vectorize(segment) for segment in preprocessed_segments_doc2]

        plagiarism_segments = []
        for vector1, segment1 in zip(vectorized_doc1, segments_doc1):
            for vector2, segment2 in zip(vectorized_doc2, segments_doc2):

                similarity1 = cosine_similarity([vector1], [vector2])
                similarity2 = calcular_similitud_coseno(segment1[0], segment2[0])
                similarity = similarity1 if similarity2 >  0.25 else (similarity1 + similarity2) /  2

                if similarity[0][0] > threshold:
                    original_segment1 = self.nlp(doc1)[segment1[1]:segment1[2]]
                    original_segment2 = self.nlp(doc2)[segment2[1]:segment2[2]]
                    plagiarism_segments.append((original_segment1, original_segment2, similarity[0][0]))
        
        plagiarism_segments = sorted(plagiarism_segments, key=lambda x: x[2], reverse=True)

        return plagiarism_segments
