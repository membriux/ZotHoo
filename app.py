from flask import Flask, url_for, render_template, request
import json
import config
import pprint

pp = pprint.PrettyPrinter()

app = Flask(__name__)

index = dict()
bookkeeping = dict()
total_tokens = 0
total_links = 0


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


def run_search(search_input):
    global total_tokens, total_links
    try:
        total_links = len(index[search_input])
        total_tokens = sum([count for count in index[search_input].values()])
        results = [bookkeeping[u] for u in sorted(index[search_input], key=index[search_input].__getitem__, reverse=True)]
        return top_twenty(results)
    except KeyError:
        return []


def top_twenty(results):
    if len(results) > 20:
        return results[:20]
    else:
        return results


def load_index():
    global index, bookkeeping
    with open('index.json', 'r') as data:
         index = json.load(data)

    with open(config.BOOKKEEPING, 'r') as data:
         bookkeeping = json.load(data)


if __name__ == '__main__':
    app.run()

