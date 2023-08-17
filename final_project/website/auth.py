from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)
#make a new route called '/login' with two methods
@auth.route('/login', methods=['Get', 'Post'])
#define a new function called login_page():
def login_page():
#check if the method is post or get, if 'get', redirect to login.html with user=current_user
#if post, get the required info 
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
#make a user variable of the current user based on email by query
        user = User.query.filter_by(email=email).first()
#check if there is a user with that email
        if user:
#if there is, check password then flash logged in successfully
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
#log in the current user
                login_user(user, remember=True)
#then return redirect to views.home
                return redirect(url_for('views.home'))
            else:
#if password is wrong, flash message
                flash('Password incorrect, please try again', category='error')
#if email does not exists, flash message
        else:
            flash('No account associated with this email', category='error')
        
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login_page'))


@auth.route('/signup', methods=['Get', 'POST'])
def sign_up():
#if method is post get required attributes
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

#make a user instance then filter it
        user = User.query.filter_by(email=email).first()

        if user:
#check if there is already an account associated with that email, flash message
            flash('Email already in use', category='error')
        
        else: 
#checks the input for len, name length and if password 1 and 2 match
#if okay, create a new user with the required attributes except for the password, generate a password hash for that one with method='sha256'
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(password1, method='sha256'))
#add that new_user as a db session and commit that session
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account successfully created!')
            return redirect(url_for('views.home'))

# if method is get and not post, render signup template
    return render_template('signup.html')

#then login that user and redirect to views.home