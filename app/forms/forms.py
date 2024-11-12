from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

from app.forms.validators import CategoryExists, LevelExists, EqualToText


class BaseForm(FlaskForm):
    submit = SubmitField("Отправить")


class LessonForm(BaseForm):
    title = StringField("Название", validators=[DataRequired(), Length(min=0, max=40)])
    category = SelectField("Категория", validators=[DataRequired(), CategoryExists()])
    level = SelectField("Сложность", validators=[DataRequired(), LevelExists()])


class CategoryForm(BaseForm):
    title = StringField("Название", validators=[DataRequired(), Length(min=0, max=40)])

