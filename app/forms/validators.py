from wtforms import ValidationError

from app.models import Category, Level, Lesson


class CategoryExists:
    def __init__(self, message=None):
        if message is None:
            message = "Выберите действительную категорию."
        self.message = message

    def __call__(self, form, field):
        category_id = field.data
        if not Category.query.get(category_id):
            raise ValidationError(self.message)


class LevelExists:
    def __init__(self, message=None):
        if message is None:
            message = 'Выберите действительную сложность.'
        self.message = message

    def __call__(self, form, field):
        level_id = field.data
        if not Level.query.get(level_id):
            raise ValidationError(self.message)


class LessonExists:
    def __init__(self, message=None):
        if message is None:
            message = "Выберите действительный урок."
        self.message = message

    def __call__(self, form, field):
        lesson_id = field.data
        if not Lesson.query.get(lesson_id):
            raise ValidationError(self.message)


class EqualToText:
    def __init__(self, text: str, message=None):
        if message is None:
            message = f'Текст должен быть равен: {text}'
        self.message = message
        self.text = text

    def __call__(self, form, field):
        field_text = field.data
        if field_text != self.text:
            raise ValidationError(self.message)
