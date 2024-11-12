from app.forms.forms import LessonForm
from app.models import Category, Level, Lesson


def fill_lesson_form(form: LessonForm):
    form.category.choices = [(category.id, f"ID: {category.id} - {category.title}") for category in Category.query.all()]
    form.level.choices = [(level.id, f"ID: {level.id} - {level.title}({level.indicator})") for level in Level.query.all()]

    return form


def fill_lesson_form_edit(form: LessonForm, lesson: Lesson):
    form.category.choices = [(category.id, f"ID: {category.id} - {category.title}") for category in Category.query.all()]
    form.level.choices = [(level.id, f"ID: {level.id} - {level.title}({level.indicator})") for level in Level.query.all()]

    form.category.choices.insert(0,
                                 (lesson.category.id, f"ID: {lesson.category.id} - {lesson.category.title} (текущая)"))
    form.level.choices.insert(0,
                              (lesson.level.id, f"ID: {lesson.level.id} - {lesson.level.title} (текущий)"))
    return form