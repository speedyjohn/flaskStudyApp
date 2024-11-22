from app.forms.forms import LessonForm, WordForm
from app.models import Category, Level, Lesson, Word


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


def fill_word_form(form: WordForm):
    form.lesson.choices = [(lesson.id, f"ID: {lesson.id} - {lesson.title}") for lesson in Lesson.query.all()]

    return form


def fill_word_form_edit(form: WordForm, word: Word):
    form.lesson_id.choices = [(lesson.id, f"ID: {lesson.id} - {lesson.title}") for lesson in Lesson.query.all()]
    form.lesson_id.choices.insert(0,
                               (word.lesson.id, f"ID: {word.lesson.id} - {word.lesson.title} (текущий)"))

    return form
