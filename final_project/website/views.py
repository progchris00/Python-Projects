from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from . import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/einstein', methods=['GET','POST'])
def einstein():
    if request.method == 'POST':
        mass = request.form.get('mass')
        result = cal_energy(int(mass))
        return render_template('result_eins.html', mass=mass, result=result)

    return render_template('einstein.html')

@views.route('/figlet')
def figlet():
    return render_template('figlet.html')

@views.route('/meal')
def meal():
    return render_template('meal.html')

@views.route('/shirtificate')
def shirt():
    return render_template('shirt.html')

