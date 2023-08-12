from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from . import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/einstein', methods=['GET','POST'])
def einstein():
    if request.method == 'POST':
        the_input = request.form.get('mass')
        the_result = cal_energy(int(the_input))
        return render_template('results.html', title='Einstein', the_input=the_input, the_result=the_result)

    return render_template('einstein.html')

@views.route('/figlet', methods=['GET','POST'])
def figlet():
    if request.method == 'POST':
        the_input = request.form.get('text')
        the_result = to_fig(the_input)
        return render_template('results.html', title='Figlet', the_input=the_input, the_result=the_result)
    
    return render_template('figlet.html')

@views.route('/meal', methods=['GET','POST'])
def meal():
    if request.method == 'POST':
        the_input = request.form.get('time')
        the_result = convert(the_input)
        return render_template('results.html', title='Meal Time', the_input=the_input, the_result=the_result)
    
    return render_template('meal.html')

@views.route('/shirtificate', methods=['GET','POST'])
def shirt():
    if request.method == 'POST':
        the_input = request.form.get('text')
        the_result = shirtify(the_input)
        return render_template('results.html', title='Shirtificate', the_input=the_input, the_result=the_result)
    
    return render_template('shirt.html')

