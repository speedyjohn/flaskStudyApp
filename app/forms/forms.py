from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

from app.forms.validators import CategoryExists, LevelExists, EqualToText, LessonExists


class BaseForm(FlaskForm):
    submit = SubmitField("Отправить")


class LessonForm(BaseForm):
    title = StringField("Название", validators=[DataRequired(), Length(min=0, max=40)])
    category_id = SelectField("Категория", validators=[DataRequired(), CategoryExists()])
    level_id = SelectField("Сложность", validators=[DataRequired(), LevelExists()])


class CategoryForm(BaseForm):
    title = StringField("Название", validators=[DataRequired(), Length(min=0, max=40)])


class LevelForm(BaseForm):
    title = StringField("Название", validators=[DataRequired(), Length(min=0, max=40)])
    indicator = IntegerField("Показатель", validators=[DataRequired()])


class WordForm(BaseForm):
    word = StringField("Слово", validators=[Length(min=0, max=40)])
    translation = StringField("Перевод", validators=[Length(min=0, max=40)])
    lesson_id = SelectField("Урок", validators=[DataRequired(), LessonExists()])
    many_rows = BooleanField("Множественный ввод", validators=[])
    words = TextAreaField("Множественный ввод", validators=[])
