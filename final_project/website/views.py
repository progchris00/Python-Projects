from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user  
from . import *

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/einstein', methods=['GET','POST'])
@login_required
def einstein():
    if request.method == 'POST':
        try: 
            the_input = request.form.get('mass')
            the_result = cal_energy(int(the_input))
            return render_template('results.html', title='Einstein', the_input=the_input, the_result=the_result, user=current_user)

        except ValueError:
            flash("Input required", category='error')

    return render_template('einstein.html', user=current_user)

@views.route('/figlet', methods=['GET','POST'])
@login_required
def figlet():
    if request.method == 'POST':
        the_input = request.form.get('text')
        the_result = to_fig(the_input)
        return render_template('results.html', title='Figlet', the_input=the_input, the_result=the_result, user=current_user)
    
    return render_template('figlet.html', user=current_user)

@views.route('/meal', methods=['GET','POST'])
@login_required
def meal():
    if request.method == 'POST':
        the_input = request.form.get('time')
        the_result = convert(the_input)
        return render_template('results.html', title='Meal Time', the_input=the_input, the_result=the_result, user=current_user)
    
    return render_template('meal.html', user=current_user)

@views.route('/shirtificate', methods=['GET','POST'])
@login_required
def shirt():
    if request.method == 'POST':
        the_input = request.form.get('text')
        the_result = shirtify(the_input)
        return render_template('results.html', title='Shirtificate', the_input=the_input, the_result=the_result, user=current_user)
    
    return render_template('shirt.html', user=current_user)

