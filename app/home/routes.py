# -*- coding: utf-8 -*-
# 0631676623

from datetime import datetime, timedelta
from app import app
from flask import render_template, redirect, flash, url_for, request
# from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Task
from werkzeug.urls import url_parse
from app import db
import os
from app.home import bp

@bp.route('/')
@bp.route('/index')
# @login_required
def index():


    return render_template("index.html", title='Home Page')
