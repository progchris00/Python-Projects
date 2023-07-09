from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    return str(search4letters(request.form['phrase'], request.form['letters']))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                           the_title='Welcome to search4letters on the web!')

@app.route('/results')
def result_page() -> 'html':
    return render_template('results.html', 
                           the_title='Welcome to search4letters on the web!',
                           the_phrase=request.form['phrase'])

app.run(debug=True)