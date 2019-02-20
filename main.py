from flask import Flask, url_for, render_template, request

app = Flask(__name__)


lst = ['Hello avocados', 'Hello world', 'Hello memo', 'Hello martin', 'Hello water', 'Hello Irvine']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['search_input'] != '':
        search_input = request.form['search_input']
        results = run_search(search_input)
        return render_template('index.html', results=results)
    else:
        return render_template('index.html')


def run_search(search_input):
    results = []
    for item in lst:
        if search_input in item:
            results.append(item)
    return results
