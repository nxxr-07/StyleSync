from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from models import db, User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter((User.username==username)|(User.email==email)).first():
            flash('User already exists!')
            return render_template('signup.html')
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Signup successful! Please sign in.')
        return redirect(url_for('auth.signin'))
    return render_template('signup.html')

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        # Admin login check
        if email == 'admin@ss' and password == 'admin@ss':
            session['user_id'] = 'admin'
            session['is_admin'] = True
            flash('Admin signed in!')
            return redirect(url_for('admin_panel'))
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['is_admin'] = False
            flash('Signed in successfully!')
            return redirect(url_for('home'))
        flash('Invalid credentials!')
    return render_template('signin.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!')
    return redirect(url_for('auth.signin'))
