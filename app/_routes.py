# -*- coding: utf-8 -*-
# 0631676623

from datetime import datetime, timedelta
from app import app
from flask import render_template, redirect, flash, url_for, request, send_from_directory
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Machine, Incub
from werkzeug.urls import url_parse
from app import db
import os
from sqlalchemy.sql import or_, and_, text
from sqlalchemy import func


basedir = os.path.abspath(os.path.dirname(__file__))



# ------------------------------------------------------------------------
# СПИСОК СВОБОДНЫХ ДОМЕНОВ ПО ЗОНЕ - КОНЕЦ
# ------------------------------------------------------------------------
@app.route('/inc_add', methods=['GET', 'POST'])
@login_required
def inc_add():
    pass

@app.route('/inc_all', methods=['GET', 'POST'])
@login_required
def inc_all():
    pass

@app.route('/inc_del', methods=['GET', 'POST'])
@login_required
def inc_del():
    pass

@app.route('/inc_end', methods=['GET', 'POST'])
@login_required
def inc_end():
    pass

@app.route('/inc_fut', methods=['GET', 'POST'])
@login_required
def inc_fut():
    pass

@app.route('/inc_now', methods=['GET', 'POST'])
@login_required
def inc_now():
    pass

@app.route('/mach_add', methods=['GET', 'POST'])
@login_required
def mach_add():
    pass

@app.route('/mach_del', methods=['GET', 'POST'])
@login_required
def mach_del():
    pass

@app.route('/mach_spis', methods=['GET', 'POST'])
@login_required
def mach_spis():
    pass

@app.route('/stat_ink', methods=['GET', 'POST'])
@login_required
def stat_ink():
    pass

@app.route('/stat_procent', methods=['GET', 'POST'])
@login_required
def stat_procent():
    pass


@app.route('/')
@app.route('/index')
@login_required
def index():


    return render_template("index.html", title='Home Page')


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)
