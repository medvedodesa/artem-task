from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Task, User
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_login import current_user
from sqlalchemy.sql import and_
from wtforms.fields.html5 import DateField, TimeField


class MachNew(FlaskForm):
    task = StringField('Название задачи', validators=[Length(min=1, max=50)])
    # user_id = QuerySelectField('Исполнитель', query_factory=lambda: User.query.order_by(User.username).all(), get_label='username')
    date_pro = DateField('Дата начала', validators=[DataRequired()])
    egg = IntegerField('Срок выполнения (в днях)')
    submit = SubmitField('Добавить')

    # Функция должна быть подключена в случае, если 2 задачи не могут иметь 1 название!!!!!
    def validate_task(self, task):
        task = Task.query.filter(and_(Task.user_id==current_user.username, Task.task==task)).first()
        if task is not None:
            raise ValidationError('Это имя уже использовано')


class MachDel(FlaskForm):
    task = QuerySelectField('Название задачи', query_factory=lambda: Task.query.order_by(Task.task).all(),
                               get_label='task')
    ja_ne_debil_i_ponial = BooleanField('Подтверждаю, задача выполнена')
    submit = SubmitField('Выполнить задачу')
