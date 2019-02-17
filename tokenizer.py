import re
from collections import Counter
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer

class Tokenizer():
    def __init__(self):
        self.stop_words = set(stopwords.words('english')) 
        self.stemmer = PorterStemmer()

    @staticmethod
    def normalize_text(corpus : str):
        temp = re.sub(r"(\\n|\\t|\\r)", ' ', corpus)  # srip newlines
        temp = re.sub(r"([^ \sa-zA-Z0-9])", ' ', corpus).lower()  # srip non ascii
        temp = re.sub(r"( +)", ' ', temp).strip()     # remove extra spaces
        return temp


    def counter_tokenize(self, corpus : str, stem=False):
        temp = self.normalize_text(corpus).split(' ')
        if self.stemmer: temp = [self.stemmer.stem(word) for word in temp]
        return Counter((word for word in temp if word not in self.stop_words) )


        