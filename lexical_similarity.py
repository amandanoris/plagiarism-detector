from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calcular_similitud_coseno(doc1_content, doc2_content):
  
    vectorizer = TfidfVectorizer()

   
    vectores = vectorizer.fit_transform([doc1_content, doc2_content])

  
    similitud_coseno = cosine_similarity(vectores[0:1], vectores[1:2])[0][0]

  
    return similitud_coseno

