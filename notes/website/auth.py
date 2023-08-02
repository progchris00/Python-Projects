from flask import Blueprint, render_template, request

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
    name = request.form['firstname']
    email = request.form['email']
    password = request.form['password1']
    return render_template('home.html',
                           the_name=name,
                           the_email=email,
                           the_password=password)