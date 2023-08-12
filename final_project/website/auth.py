from flask import Blueprint, render_template, request, flash, redirect, url_for


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password", category='error')
        else:
            flash("Email does not exists", category='error')

    return render_template('login.html', user=current_user)


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