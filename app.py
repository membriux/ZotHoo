from flask import Flask, url_for, render_template, request, session
from flask_paginate import Pagination, get_page_args
from math import log10

from src.tokenizer import Tokenizer
from src.document import Document
import config

import json
import nltk
import os

nltk.download('stopwords')


app = Flask(__name__)
app.secret_key = os.urandom(8)

Index = dict()
Header = dict()
bookkeeping = dict()

search_input = ''

total = []

N_documents = None
N_tokens = None
tokenizer = Tokenizer()


@app.before_request
def setup():
    global search_input
    if 'user' not in session:
        search_input = ''


@app.route('/', methods=['GET', 'POST'])
def main():
    global search_input, Index, bookkeeping, total
    if Index == {}:
        load_index()


    s = run_search(search_input)
    total, total_links, total_tokens = s['tr'], s['tl'], s['tt']
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    if request.method == 'POST':
        session['user'] = os.urandom(8)
        search_input = request.form['search_input']
        s = run_search(search_input)
        total, total_links, total_tokens = s['tr'], s['tl'], s['tt']
        page, per_page, offset = get_page_args(page_parameter='1', per_page_parameter='per_page')


    pagination_links = get_results(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=len(total), css_framework='bootstrap4')

    return render_template('index.html',search=search_input,
                           links=total_links, tokens=total_tokens,
                           all_tokens=N_tokens, all_documents=N_documents,
                           results=pagination_links, per_page=per_page,
                           page=page, pagination=pagination)


def get_results(offset=0, per_page=5):
    return total[offset: offset + per_page]



def tfidf(x, N) -> float:
    return x * log10(N_documents / N)


def run_search(search_input):
    global total_tokens, total_links, total_results
    try:
        processed_query = tokenizer.tokenize_query(search_input)
        results = set()
        total_tokens = 0
        total_links = 0
        for query in processed_query:
            total_links += len(Index[query])
            total_tokens += sum([count for count in Index[query].values()])
            tfidf_scores = [(k, tfidf(v, len(Index[query]) ) ) for k, v in Index[query].items()]
            results.add((i for i in tfidf_scores))
        total_results = [Document(bookkeeping[u], Header[u]) for u, v in sorted(tfidf_scores, key=lambda x: x[1], reverse=True)][:config.TOP_N_results]
        return {'tr': total_results, 'tl': total_links,'tt': total_tokens}
    except KeyError:
        print("[ERROR] Empty query. Raw: \"{}\", Processed: \"{}\"]".format(search_input, processed_query))
        return {'tr': [], 'tl': 0,'tt': 0}


def load_index():
    global Index, Header, bookkeeping, N_documents, N_tokens
    print('reading')
    with open(config.INDEX_PATH, 'r') as data:
        Index = json.load(data)

    with open(config.HEADER_PATH, 'r') as data:
        Header = json.load(data)

    with open(config.BOOKKEEPING, 'r') as data:
        bookkeeping = json.load(data)

    N_documents = len(bookkeeping)
    N_tokens = len(Index)


if __name__ == '__main__':
    app.run()
