from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calcular_similitud_coseno(doc1_content, doc2_content):
    """
    Calcula la similitud coseno entre dos documentos.

    Esta función utiliza TfidfVectorizer de sklearn para transformar los documentos
    en vectores TF-IDF y luego calcula la similitud coseno entre estos vectores.

    Parámetros:
    - doc1_content (str): El contenido del primer documento.
    - doc2_content (str): El contenido del segundo documento.

    Retorna:
    - float: La similitud coseno entre los dos documentos.
    """
    vectorizer = TfidfVectorizer()
    vectores = vectorizer.fit_transform([doc1_content, doc2_content])
    similitud_coseno = cosine_similarity(vectores[0:1], vectores[1:2])[0][0]
    return similitud_coseno

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show(document, filename):
    """
    Genera y guarda una nube de palabras para un documento.

    Esta función utiliza la biblioteca wordcloud para generar una nube de palabras
    basada en el contenido del documento proporcionado. La imagen resultante se guarda
    en el directorio 'static/images' con el nombre de archivo especificado.

    Parámetros:
    - document (str): El texto del documento para el cual se generará la nube de palabras.
    - filename (str): El nombre del archivo para guardar la imagen de la nube de palabras.

    Retorna:
    - None
    """
    wordcloud = WordCloud(width =   800, height =   800,
                          background_color ='white',
                          min_font_size =   10).generate(document)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    os.makedirs('static/images', exist_ok=True)
    plt.savefig(f'static/images/{filename}.png')
    plt.close()
