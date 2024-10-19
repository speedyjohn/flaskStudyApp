from app.models import Lesson, Category, Level, Word


def count_rows():
    lessons_count = Lesson.query.count()
    categories_count = Category.query.count()
    levels_count = Level.query.count()
    words_count = Word.query.count()
    return {
        "lessons_count": lessons_count,
        "categories_count": categories_count,
        "levels_count": levels_count,
        "words_count": words_count
    }
