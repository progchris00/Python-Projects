from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user  
from .models import User, Comments
from . import *
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/einstein', methods=['GET', 'POST'])
@login_required
def einstein():
    all_comments = Comments.query.all()
    if request.method == 'POST':
        try: 
            the_input = request.form.get('mass')
            the_result = cal_energy(int(the_input))
            return render_template('results.html', title='Einstein', the_input=the_input, the_result=the_result, user=current_user)

        except ValueError:
            flash("Input required", category='error')
    
    return render_template('einstein.html', user=current_user, all_comments=all_comments)


@views.route('/figlet', methods=['GET','POST'])
@login_required
def figlet():
    if request.method == 'POST':
        the_input = request.form.get('text')
        the_result = to_fig(the_input)
        return render_template('results.html', title='Figlet', the_input=the_input, the_result=the_result, user=current_user)
    
    return render_template('figlet.html', user=current_user)


@views.route('/meal', methods=['GET','POST'])
@login_required
def meal():
    if request.method == 'POST':
        the_input = request.form.get('time')
        the_result = convert(the_input)
        return render_template('results.html', title='Meal Time', the_input=the_input, the_result=the_result, user=current_user)
    
    return render_template('meal.html', user=current_user)


@views.route('/shirtificate', methods=['GET','POST'])
@login_required
def shirt():
    if request.method == 'POST':
        the_input = request.form.get('text')
        the_result = shirtify(the_input)
        return render_template('results.html', title='Shirtificate', the_input=the_input, the_result=the_result, user=current_user)
    
    return render_template('shirt.html', user=current_user)


@views.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    if request.method == 'POST':
        return redirect(url_for('views.update'))
    
    return render_template('profile.html', user=current_user)


@views.route('/update', methods=['GET','POST'])
@login_required
def update():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        email = request.form.get('email')

        user = User.query.get(current_user.id)
        user.first_name = first_name
        user.email = email
        db.session.commit()

        flash('Updated succesfully!')
        return redirect(url_for('views.profile'))

    return render_template("update.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_comment():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Comments.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})


@views.route('/einstein-comments', methods=['GET','POST'])
@login_required
def add_comments():
    if request.method == 'POST':
        comment = request.form.get('comment')
        new_comment = Comments(data=comment, user_id=current_user.id,)
        db.session.add(new_comment)
        db.session.commit()
        flash("Comment added!", category='success')
    
    all_comments = Comments.query.all()
    return render_template('einstein.html', user=current_user, all_comments=all_comments)