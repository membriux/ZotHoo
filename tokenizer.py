import re
from collections import Counter
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

class Tokenizer():
    def __init__(self, token_processing="stem"):
        self.stop_words = set(stopwords.words('english')) 
        self.stop_words.add('')
        self.token_processor = None

        if token_processing == "stem":
            self.token_processor = PorterStemmer()


    @staticmethod
    def normalize_text(corpus : str):
        corpus = re.sub(r'\n|\t', '', corpus)  # srip newlines
        corpus = re.sub(r"([^ \sa-zA-Z0-9])", ' ', corpus).lower()  # srip non alphanumeric
        corpus = re.sub(r'[^\x00-\x7F]+', ' ', corpus).lower()  # srip non ascii
        corpus = re.sub(r"( +)", ' ', corpus).strip()     # remove extra spaces
        return corpus

    def counter_tokenize(self, corpus : str):
        corpus = self.normalize_text(corpus).split(' ')
        if self.token_processor: corpus = [self.token_processor.stem(word) for word in corpus]
        return Counter((word for word in corpus if word not in self.stop_words and len(word) > 1))

    def tokenize_query(self, query : str):
        """
        assuming query is a single token
        """
        query = self.normalize_text(query)
        query = query.split(' ')
        if self.token_processor: query = [self.token_processor.stem(q) for q in query]
        return query

