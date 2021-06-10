
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))





class Task(db.Model):
    # __tablename__='Mach'
    id=db.Column(db.Integer, primary_key=True) # Номер задачи (общий)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Исполнитель
    user_add =db.Column(db.Integer, db.ForeignKey('user.id')) # Кто выдал задачу
    user_del = db.Column(db.Integer, db.ForeignKey('user.id'), default=None)  # Кто удалил задачу
    task = db.Column(db.String(50)) # Имя задачи
    date_pro = db.Column(db.DateTime) # Дата начала
    date_add = db.Column(db.DateTime, default=datetime.datetime.now) # Дата добавления
    date_del= db.Column(db.DateTime) # Дата удаления
    date_end= db.Column(db.DateTime) # Дата окончания
    status = db.Column(db.Boolean, default=False) # Статус
    cicle=db.Column(db.Integer) # Количество циклов продления


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # Номер сотрудника
    username = db.Column(db.String(64), index=True, unique=True)# Логин
    email = db.Column(db.String(120), index=True, unique=True)# Почта (НАДО?)
    password_hash = db.Column(db.String(128))# Служебное
    about_me = db.Column(db.String(140))# О сотруднике
    last_seen = db.Column(db.DateTime, default=datetime.datetime.utcnow)# Последнее время посещения

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
