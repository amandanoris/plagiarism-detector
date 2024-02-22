import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import spacy
from transformers import BertModel, BertTokenizer

nlp = spacy.load('en_core_web_sm')

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

class TextPreprocessor:
    """
    Clase para preprocesar texto, incluyendo la conversión a minúsculas, eliminación de puntuación,
    expansión de contracciones, lematización y estemización.

    Parámetros:
    - language (str): El idioma del texto a preprocesar. Por defecto es 'english'.
    """
    def __init__(self, language='english'):
        """
        Inicializa el preprocesador de texto con conjuntos de palabras de parada, un estemizador y un lematizador.
        """
        self.stop_words = set(stopwords.words(language))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.contractions_dict = {"ain't": "are not","'s":" is","aren't": "are not"}
        self.contractions_re = re.compile('(%s)' % '|'.join(self.contractions_dict.keys()))
        
    def preprocess(self, text):
        """
        Preprocesa el texto pasando por varias etapas de limpieza y transformación.

        Parámetros:
        - text (str): El texto a preprocesar.

        Retorna:
        - str: El texto preprocesado.
        """
        text = self.to_lowercase(text)
        text = self.remove_punctuation(text)
        text = self.expand_contractions(text)
        text = self.lemmatize_words(text)
        return text

    def tokenize(self, text):
        """
        Tokeniza el texto en palabras.

        Parámetros:
        - text (str): El texto a tokenizar.

        Retorna:
        - list: Una lista de tokens.
        """
        return nltk.word_tokenize(text)

    def to_lowercase(self, text):
        """
        Convierte el texto a minúsculas.

        Parámetros:
        - text (str): El texto a convertir.

        Retorna:
        - str: El texto convertido a minúsculas.
        """
        return text.lower()

    def remove_punctuation(self, text):
        """
        Elimina la puntuación del texto.

        Parámetros:
        - text (str): El texto del que eliminar la puntuación.

        Retorna:
        - str: El texto sin puntuación.
        """
        return re.sub(r'[^\w\s]', '', text)

    def remove_stopwords(self, text):
        """
        Elimina las palabras de parada del texto.

        Parámetros:
        - text (str): El texto del que eliminar las palabras de parada.

        Retorna:
        - list: Una lista de tokens sin palabras de parada.
        """
        word_tokens = self.tokenize(text)
        return [word for word in word_tokens if word not in self.stop_words]

    def stem_words(self, text):
        """
        Aplica estemización a las palabras del texto.

        Parámetros:
        - text (str): El texto a estemizar.

        Retorna:
        - str: El texto con palabras estemizadas.
        """
        word_tokens = self.remove_stopwords(text)
        return " ".join([self.stemmer.stem(word) for word in word_tokens])

    def lemmatize_words(self, text):
        """
        Aplica lematización a las palabras del texto.

        Parámetros:
        - text (str): El texto a lematizar.

        Retorna:
        - str: El texto con palabras lematizadas.
        """
        word_tokens = self.remove_stopwords(text)
        return " ".join([self.lemmatizer.lemmatize(word) for word in word_tokens])

    def expand_contractions(self, text, contractions_dict=None):
        """
        Expande las contracciones en el texto.

        Parámetros:
        - text (str): El texto del que expandir las contracciones.
        - contractions_dict (dict): Un diccionario de contracciones a expandir. Por defecto se utiliza el diccionario interno.

        Retorna:
        - str: El texto con contracciones expandidas.
        """
        if contractions_dict is None:
            contractions_dict = self.contractions_dict
        def replace(match):
            return contractions_dict[match.group(0)]
        return self.contractions_re.sub(replace, text)

    def tokenize_text(self, text):
        """
        Tokeniza el texto en palabras.

        Parámetros:
        - text (str): El texto a tokenizar.

        Retorna:
        - list: Una lista de tokens.
        """
        tokens = self.tokenize(text)
        return tokens
