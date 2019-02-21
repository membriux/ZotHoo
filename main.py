from flask import Flask, url_for, render_template, request
import json
import config
import pprint

pp = pprint.PrettyPrinter()

app = Flask(__name__)

index = dict()
bookkeeping = dict()


@app.route('/', methods=['GET', 'POST'])
def index():
    global index, bookkeeping
    load_index()
    if request.method == 'POST' and request.form['search_input'] != '':
        search_input = request.form['search_input']
        results = run_search(search_input)
        return render_template('index.html', results=results, search=search_input)
    else:
        return render_template('index.html')


def run_search(search_input):
    return [bookkeeping[u] for u in sorted(index[search_input], key=index[search_input].__getitem__, reverse=True)]


def load_index():
    global index, bookkeeping
    with open('index.json', 'r') as data:
         index = json.load(data)

    with open(config.BOOKKEEPING, 'r') as data:
         bookkeeping = json.load(data)



