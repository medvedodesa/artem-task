# -*- coding: utf-8 -*-
# 0631676623

from datetime import datetime, timedelta
from app import app
from flask import render_template, redirect, flash, url_for, request, send_from_directory
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Task
from werkzeug.urls import url_parse
from app import db
import os
from sqlalchemy.sql import and_, text
from sqlalchemy import func
from app.mach import bp
from app.mach.forms import MachNew, MachDel


@bp.route('/mach_add', methods=['GET', 'POST'])
@login_required
def mach_add():
    form = MachNew()
    if form.validate_on_submit():
        egg = form.egg.data
        date = form.date_pro.data
        date_end=date+timedelta(days=egg)
        task = form.task.data,
        print(date)
        new = Task(task=task, user_id=current_user.username, user_add=current_user.username, date_pro=date, date_end=date_end,
                      cicle=0)
        print(form.date_pro.data, type(form.date_pro.data))
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('mach.mach_spis'))
    else:
        return render_template('mach/mach_add.html', title='Add new machine', form=form)


@bp.route('/mach_del', methods=['GET', 'POST'])
@login_required
def mach_del():
    form = MachDel()
    if form.validate_on_submit():
        if form.ja_ne_debil_i_ponial.data is True:

            x = form.task.data
            z = x.task
            ob = Task.query.filter_by(task=z).first()
            ob.status=True
            # db.session.delete(ob)
            db.session.commit()
            return redirect(url_for('mach.mach_spis'))
        else:

            return render_template('deltypetov.html', form=form)
    else:
        return render_template("mach/mach_del.html", title='Delete machine', form=form)


@bp.route('/mach_spis', methods=['GET', 'POST'])
@login_required
def mach_spis():
    data = Task.query.filter(and_(Task.user_id == current_user.id, Task.status == False)).order_by(Task.task).all()
    count = Task.query.filter(and_(Task.user_id == current_user.id, Task.status == False)).order_by(Task.task).count()
    return render_template("mach/mach_spis.html", title='List task', items=data, count=count)
