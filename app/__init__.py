from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.static_folder = 'static'

from app import models
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp, url_prefix='/errors')
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
from app.mach import bp as mach_bp
app.register_blueprint(mach_bp, url_prefix='/mach')

from app.home import bp as home_bp
app.register_blueprint(home_bp)



from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



from app.models import User, Task

class MyUserAdmin(ModelView):
    column_exclude_list = ('password_hash',)
    column_hide_backrefs = False

from sqlalchemy import inspect

class ChildView(ModelView):
    column_display_pk = False # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = [c_attr.key for c_attr in inspect(Task).mapper.column_attrs]




app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='SEMExperts CRM', template_mode='bootstrap3')
admin.add_view(MyUserAdmin(User, db.session, name='User'))

admin.add_view(ChildView(Task, db.session, name='Task'))

# admin.add_view(ModelView(Task, db.session, name='Task'))
