from flask import Flask, render_template, request, url_for
import ortiz as ort

app = Flask(__name__)

@app.route('/')
@app.route('/start')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='CS50P Final Project')


@app.route('/einstein')
def einstein() -> 'html':
    return render_template('einstein.html')


@app.route('/meal')
def meal_time() -> 'html':
    return render_template('meal.html')


@app.route('/figlet')
def figlet() -> 'html':
    return render_template('figlet.html')


@app.route('/shirtificate')
def shirt() -> 'html':
    return render_template('shirt.html')


@app.route('/result/eins', methods=['POST'])
def result_eins() -> 'html':
    mass = request.form['mass']
    result = ort.cal_energy(int(mass))
    return render_template('result_eins.html',
                           the_result = result,
                           the_mass = mass)


@app.route('/result/meal', methods=['POST'])
def result_meals() -> 'html':
    inpt = request.form['time']
    result = ort.convert(inpt)
    return render_template('result_meal.html',
                           the_result = result,
                           the_inpt = inpt)


@app.route('/result/fig', methods=['POST'])
def result_fig() -> 'html':
    inpt = request.form['text']
    result = ort.to_fig(inpt)
    return render_template('result_fig.html',
                           the_result = result,
                           the_inpt = inpt)


@app.route('/result/shirt', methods=['POST'])
def result_shirt() -> 'html':
    inpt = request.form['text']
    ort.shirtify(inpt)
    pdf_url = url_for('static', filename='shirtificate.pdf')
    return render_template('result_shirt.html',
                           pdf_url=pdf_url,
                           the_inpt = inpt)


if __name__ =='__main__':
    app.run(debug=True)