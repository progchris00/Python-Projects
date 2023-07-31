from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page() -> 'html':
    return render_template('login.html',
                            the_title = "Login")

@auth.route('/signup')
def signup_page() -> 'html':
    return render_template('signup.html',
                            the_title = "Sign Up")