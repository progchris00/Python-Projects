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

# @app.route('/result')
# def entry_page() -> 'html':
#     return render_template('result.html', 
#                            the_title='Welcome to search4letters on the web!',
#                            the_phrase=phrase
#                            the_letters=letters
#                            the_result=)

app.run(debug=True)