from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h2> Hello World </h2>"