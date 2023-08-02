from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page() -> 'html':
    return render_template('login.html')

@auth.route('/sign-up')
def signup_page() -> 'html':
    return render_template('signup.html',
                            the_title = "Testing")

@auth.route('/home', methods=['POST'])
def home_page() -> 'html':
    return render_template('home.html')