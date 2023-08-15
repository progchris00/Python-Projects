from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# from . import db
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
                return redirect('views.home')
            else:
#if password is wrong, flash message
                flash('Password incorrect, please try again', category='error')
#if email does not exists, flash message
        else:
            flash('No account associated with this email', category='error')
        
    return redirect('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login_page'))


@auth.route('/signup', methods=['Get', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('firstname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')

        elif len(email.split('@')[0]) < 3:
            flash("Username must be 3 characters long", category='error')
        elif len(name) < 3:
            flash("Name must be 3 characters long.", category='error')
        elif password1 != password2:
            flash("Passwords do not match", category='error')
        else:
            new_user = User(email=email, first_name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account succesfully created!")
            return redirect(url_for('views.home'))


    return render_template('signup.html', user=current_user)