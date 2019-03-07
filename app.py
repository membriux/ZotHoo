from flask import Flask, url_for, render_template, request
from flask_paginate import Pagination, get_page_args
from math import log10
from tokenizer import Tokenizer
import json
import config
import pprint

pp = pprint.PrettyPrinter()

app = Flask(__name__)

index = dict()
bookkeeping = dict()

search_input = ''


total_results = []
total_tokens = 0
total_links = 0
N_documents = None
N_tokens = None
tokenizer = Tokenizer()



@app.route('/', methods=['GET', 'POST'])
def index():
    global search_input, index, bookkeeping, total_tokens, total_links

    if request.method == 'POST' and request.form['search_input'] != '':
        search_input = request.form['search_input']
        run_search(search_input)
        if len(total_results) == 0:
            search_input = 'No results for', search_input

    total = len(total_results)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_links = get_results(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('index.html',search=search_input,
                           links=total_links, tokens=total_tokens,
                           all_tokens=N_tokens, all_documents=N_documents,
                           results=pagination_links, per_page=per_page,
                           page=page, pagination=pagination)


def get_results(offset=0, per_page=10):
    return total_results[offset: offset + per_page]


def tfidf(x, N) -> float:
    return x * log10(N_documents / N)


def run_search(search_input):
    global total_tokens, total_links, total_results
    try:
        processed_query = tokenizer.tokenize_query(search_input)
        results = set()
        for query in processed_query:
            total_links += len(index[query])
            total_tokens += sum([count for count in index[query].values()])
            tfidf_scores = [(k, tfidf(v, len(index[query]) ) ) for k, v in index[query].items()]
            results.add((i for i in tfidf_scores))
        total_results = [bookkeeping[u] for u, v in sorted(tfidf_scores, key=lambda x: x[1], reverse=True)][:config.TOP_N_results]

    except KeyError:
        print("[ERROR] Empty query. Raw: \"{}\", Processed: \"{}\"]".format(search_input, processed_query))
        return []


def load_index():
    global index, bookkeeping, N_documents, N_tokens
    with open(config.INDEX_PATH, 'r') as data:
        index = json.load(data)

    with open(config.BOOKKEEPING, 'r') as data:
        bookkeeping = json.load(data)

    N_documents = len(bookkeeping)
    N_tokens = len(index)


if __name__ == '__main__':
    load_index()
    app.run(debug=True)
