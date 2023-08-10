from flask import Blueprint, render_template, request, flash, jsonify


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home() -> 'html':
    return render_template('entry.html')
