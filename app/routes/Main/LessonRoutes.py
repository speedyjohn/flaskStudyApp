from flask import Blueprint, render_template

from app.models import Lesson


class LessonRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp

        self.bp.add_url_rule("/lessons", view_func=self.get_all)
        self.bp.add_url_rule("/lessons/<int:id>", view_func=self.get_by_id)

    def get_all(self):
        lessons = Lesson.query.all()
        return render_template("lessons/index.html", lessons=lessons)

    def get_by_id(self, id):
        lesson = Lesson.query.get(id)
        return render_template("lessons/single.html", lesson=lesson)

