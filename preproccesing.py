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
    def __init__(self, language='english'):
        self.stop_words = set(stopwords.words(language))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.contractions_dict = {"ain't": "are not","'s":" is","aren't": "are not"}
        self.contractions_re = re.compile('(%s)' % '|'.join(self.contractions_dict.keys()))
        
    def preprocess(self, text):
        text = self.to_lowercase(text)
        text = self.remove_punctuation(text)
        text = self.expand_contractions(text)
        text = self.lemmatize_words(text)
        return text

    def tokenize(self, text):
        return nltk.word_tokenize(text)

    def to_lowercase(self, text):
        return text.lower()

    def remove_punctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)

    def remove_stopwords(self, text):
        word_tokens = self.tokenize(text)
        return [word for word in word_tokens if word not in self.stop_words]

    def stem_words(self, text):
        word_tokens = self.remove_stopwords(text)
        return " ".join([self.stemmer.stem(word) for word in word_tokens])

    def lemmatize_words(self, text):
        word_tokens = self.remove_stopwords(text)
        return " ".join([self.lemmatizer.lemmatize(word) for word in word_tokens])

    def expand_contractions(self, text, contractions_dict=None):
        if contractions_dict is None:
            contractions_dict = self.contractions_dict
        def replace(match):
            return contractions_dict[match.group(0)]
        return self.contractions_re.sub(replace, text)
