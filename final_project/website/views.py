from flask import Blueprint, render_template, request, flash, jsonify


views = Blueprint('views', __name__)

@views.route('/')
def home() -> 'html':
    return render_template('home.html')


@views.route('/einstein')
def einstein():
    return render_template('einstein.html')