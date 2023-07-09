from flask import Flask, render_template, request
from besh import besh_it

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello Beshy ko'

@app.route('/beshyko', methods=['POST'])
def beshers() -> 'html':
    phrase = request.form['phrase']
    result = str(besh_it(phrase))
    title = "Result"
    return render_template('result.html',
                           the_result = result,
                           the_title = title,
                           the_phrase = phrase)

@app.route('/start')
def entry_page() -> 'html':
    return render_template('entry.html', 
                           the_title='Welcome to besh it!')

app.run(debug=True)
    