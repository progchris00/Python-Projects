from flask import Flask, render_template, request
from besh import besh_it

app = Flask(__name__)

@app.route('/beshyko', methods=['POST'])
def beshers() -> 'html':
    phrase = request.form['phrase']
    result = str(besh_it(phrase))
    title = "Result"
    return render_template('result.html',
                           the_result = result,
                           the_title = title,
                           the_phrase = phrase)

@app.route('/')
@app.route('/start')
def entry_page() -> 'html':
    return render_template('entry.html', 
                           the_title='Welcome to besh it!')

if __name__ == '__main__':
    app.run(debug=True)
    