from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from .preproccesing import TextPreprocessor

# Crear una instancia de TextPreprocessor
preprocessor = TextPreprocessor(language='english')

def train_word2vec(texts, vector_size=100, window_size=5, min_count=1, epochs=10):
    """
    Entrena un modelo Word2Vec con los textos proporcionados.

    Utiliza la biblioteca gensim para entrenar un modelo Word2Vec con los textos
    preprocesados. Los textos deben ser una lista de cadenas de texto.

    Parámetros:
    - texts (list): Lista de textos para entrenar el modelo.
    - vector_size (int): Tamaño de los vectores de características.
    - window_size (int): Tamaño de la ventana de palabras para entrenar el modelo.
    - min_count (int): Número mínimo de ocurrencias de una palabra para ser incluida en el modelo.
    - epochs (int): Número de épocas para entrenar el modelo.

    Retorna:
    - Word2Vec: Modelo Word2Vec entrenado.
    """
    processed_texts = [preprocessor.tokenize_text(text) for text in texts]
    model = Word2Vec(processed_texts, vector_size=vector_size, window=window_size, min_count=min_count, epochs=epochs)
    return model

def get_document_vector(model, document):
    """
    Genera el vector de características de un documento a partir del modelo Word2Vec.

    Utiliza el modelo Word2Vec para generar un vector de características para un documento,
    promediando los vectores de características de cada palabra en el documento.

    Parámetros:
    - model (Word2Vec): Modelo Word2Vec entrenado.
    - document (str): Documento para el cual se generará el vector de características.

    Retorna:
    - numpy.ndarray: Vector de características del documento.
    """
    processed_document = preprocessor.tokenize_text(document)
    document_vector = sum([model.wv[word] for word in processed_document])
    return document_vector / len(processed_document)

def semantic_similarity(model, document1, document2):
    """
    Calcula la similitud semántica entre dos documentos.

    Utiliza el modelo Word2Vec y la similitud coseno para calcular la similitud semántica
    entre dos documentos.

    Parámetros:
    - model (Word2Vec): Modelo Word2Vec entrenado.
    - document1 (str): Primer documento para comparar.
    - document2 (str): Segundo documento para comparar.

    Retorna:
    - float: Similitud semántica entre los dos documentos.
    """
    vector1 = get_document_vector(model, document1)
    vector2 = get_document_vector(model, document2)
    return cosine_similarity([vector1], [vector2])[0][0]

def calcular_similitud_semantica(doc1_content, doc2_content):
    """
    Calcula la similitud semántica entre dos documentos utilizando Word2Vec.

    Entrena un modelo Word2Vec con los documentos proporcionados, luego calcula la similitud
    semántica entre los documentos utilizando la similitud coseno.

    Parámetros:
    - doc1_content (str): Contenido del primer documento.
    - doc2_content (str): Contenido del segundo documento.

    Retorna:
    - float: Similitud semántica entre los dos documentos.
    """
    docs = [doc1_content, doc2_content]
    model = train_word2vec(docs)

    similarity = semantic_similarity(model, doc1_content, doc2_content)

    return similarity
