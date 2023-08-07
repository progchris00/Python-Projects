from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page():
    return render_template('login.html')

@auth.route('/signup', methods=['Get', 'POST'])
def sign_up():
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
            new_user = User(email=email, first_name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account succesfully created!")
            return redirect(url_for('views.home'))


    return render_template('signup.html')