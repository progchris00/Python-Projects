from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page():
    return render_template('login.html')

@auth.route('/signup', methods=['Get', 'POST'])
def home_page():
    if request.method == 'POST':
        name = request.form.get('firstname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email.split('@')[0]) < 3:
            flash("Username must be 3 characters long", category='error')
        if len(name) < 3:
            flash("Name must be 3 characters long.", category='error')
        if password1 != password2:
            flash("Passwords do not match", category='error')
        else:
            flash("Account succesfully created!")

    return render_template('signup.html')