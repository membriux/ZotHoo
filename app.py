from math import log10
from flask import Flask, url_for, render_template, request
from tokenizer import Tokenizer
import json
import config
import pprint

pp = pprint.PrettyPrinter()

app = Flask(__name__)

index = dict()
bookkeeping = dict()
total_tokens = 0
total_links = 0
N_documents = None
tokenizer = Tokenizer()


@app.route('/', methods=['GET', 'POST'])
def index():
    global index, bookkeeping, total_tokens, total_links
    load_index()
    if request.method == 'POST' and request.form['search_input'] != '':
        search_input = request.form['search_input']
        results = run_search(search_input)
        if len(results) == 0:
            search_input = 'No results for', search_input
        return render_template('index.html',
                               results=results, search=search_input,
                               links=total_links, tokens=total_tokens)
    else:
        return render_template('index.html')

def tfidf(x, N) -> float:
    return x * log10(N_documents / N)

def run_search(search_input):
    global total_tokens, total_links
    try:
        processed_query = tokenizer.tokenize_query(search_input)
        print(processed_query)
        total_links = len(index[processed_query])
        total_tokens = sum([count for count in index[processed_query].values()])
        tfidf_scores = [(k, tfidf(v, len(index[processed_query]) ) ) for k, v in index[processed_query].items()]
        return [bookkeeping[u] for u,v in sorted(tfidf_scores, key=lambda x : x[1], reverse=True)][:config.TOP_N_results]
    except KeyError:
        print("[ERROR] Empty query. Raw: \"{}\", Processed: \"{}\"]".format(search_input, processed_query))
        return []


def load_index():
    global index, bookkeeping, N_documents
    with open(config.INDEX_PATH, 'r') as data:
         index = json.load(data)

    with open(config.BOOKKEEPING, 'r') as data:
         bookkeeping = json.load(data)

    N_documents = len(bookkeeping)


if __name__ == '__main__':
    app.run()

