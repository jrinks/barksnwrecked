from . import bp as auth
from app import db, mail
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from flask_mail import Message
from werkzeug.security import check_password_hash 
from .models import User
from .forms import UserInfoForm, LoginForm

@auth.route('/register', methods=['GET','POST'])
def register():
    title = 'SIGN UP'
    form = UserInfoForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        phone = form.phone.data
        # print(username, email, password)
        existing_user = User.query.filter((User.username == username) | (User.email == email) | (User.phone == phone)).all()
        if existing_user:
            flash("Hey, looks like you're with us already. Please try again or login with a different username and password.", 'danger')
            return redirect(url_for('auth.register'))
        
        new_user = User(username, email, password, phone)
        db.session.add(new_user)
        db.session.commit()
        
        flash(f'Thank you {username} for signing up!', 'success')
        
        msg = Message(f'Thanks, {username}', recipients=[email])
        msg.body = f'{username}, thank you so much for becoming Barks N Wrecked Insider. Please enjoy your stay, and thanks again for choosing Barks N Wrecked!'
        mail.send(msg)
        
        return redirect(url_for('main.index'))
    
    return render_template('register.html', title=title, form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    title = 'LOGIN'
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Looks like this username or password does not work. Please try again.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        flash("Nice, you're logged in and good to go!", 'success')
        return redirect(url_for('main.index'))
    
    return render_template('login.html', title=title, form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("Successfully logged out. See you next time!", 'primary')
    return redirect(url_for('main.index'))