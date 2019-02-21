import re
from collections import Counter
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer

class Tokenizer():
    def __init__(self):
        self.stop_words = set(stopwords.words('english')) 
        self.stop_words.add('')
        self.stemmer = PorterStemmer()

    @staticmethod
    def normalize_text(corpus : str):
        corpus = re.sub(r'\n|\t', '', corpus)  # srip newlines
        corpus = re.sub(r"([^ \sa-zA-Z0-9])", ' ', corpus).lower()  # srip non alphanumeric
        corpus = re.sub(r'[^\x00-\x7F]+', ' ', corpus).lower()  # srip non ascii
        corpus = re.sub(r"( +)", ' ', corpus).strip()     # remove extra spaces
        return corpus


    def counter_tokenize(self, corpus : str, stem=False):
        corpus = self.normalize_text(corpus).split(' ')
        if self.stemmer: corpus = [self.stemmer.stem(word) for word in corpus]
        return Counter((word for word in corpus if word not in self.stop_words and len(word) > 1) )


        