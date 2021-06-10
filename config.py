import os
basedir = os.path.abspath(os.path.dirname(__file__))

# heroku run python manage.py db upgrade
#
# class Config(object):
#     # POSTS_PER_PAGE = 30
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#          'sqlite:///' + os.path.join(basedir, 'sqlite.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False



class Config(object):
    POSTS_PER_PAGE = 35
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'artem100artem200'
    SQLALCHEMY_DATABASE_URI = 'postgres://xagpadsuyydyhx:fd8598868f29a80b3dc52d1da7e41eb805796e180fb360391798b9d8f565b464@ec2-54-155-208-5.eu-west-1.compute.amazonaws.com:5432/dfblqcjqgvfeep'