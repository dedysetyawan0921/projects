from models import User
from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, login_required, current_user, logout_user
from config import db, bcrypt
from users.form import CreateUser, Login


user = Blueprint('user', __name__)


@user.route('/create_user', methods = ['GET', 'POST'])
@login_required
def create_user():
    form = CreateUser()
    if request.method == 'POST' and form.validate():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  
        user = User(username=form.username.data, email=form.email.data, password=hashed)   
        db.session.add(user)
        db.session.commit()
        flash('User berhasil dibuat', 'success')
        return redirect(url_for('user.create_user'))
    return render_template('register.html', form=form)


@user.route('/', methods=['GET',  'POST'])
@user.route('/login', methods=['GET',  'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))
    form = Login()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Login Success', 'success')
            return redirect(next_page) if next_page else redirect(url_for('user.home'))
        else:
            flash('Login Unsuccessfull', 'danger')
    return render_template('login.html', title=Login, form=form)

@user.route('/logout')
def logout():
    logout_user()
    flash('Youare Logout')
    return  redirect(url_for('user.login'))

@user.route('/home')
def home():
    return render_template('home.html')