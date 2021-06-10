import os
basedir = os.path.abspath(os.path.dirname(__file__))

# heroku run python manage.py db upgrade
#
class Config(object):
    # POSTS_PER_PAGE = 30
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
         'sqlite:///' + os.path.join(basedir, 'sqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



# # Artem-dev
# class Config(object):
#     POSTS_PER_PAGE = 35
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = ''
#     SQLALCHEMY_DATABASE_URI = ''