from flask import Blueprint, render_template

from models import Lesson


class AdminLessonRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp

        self.bp.add_url_rule("/admin/lessons/", view_func=self.get_all)
        self.bp.add_url_rule("/admin/lessons/<int:id>", view_func=self.get_by_id)

    def get_all(self):
        lessons = Lesson.query.all()
        return render_template("admin/lessons/index.html", lessons=lessons)

    def get_by_id(self, id):
        lesson = Lesson.query.get(id)
        return render_template("admin/lessons/view.html", lesson=lesson)

    def create(self):
        pass

    def insert(self):
        pass

    def edit(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
