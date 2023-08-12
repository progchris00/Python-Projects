from flask import Blueprint, render_template, request, flash, jsonify


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/einstein')
def einstein():
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
