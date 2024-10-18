from flask import Blueprint, render_template, request, redirect

from models import Lesson, db


class AdminLessonRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp

        self.bp.add_url_rule("/admin/lessons/", view_func=self.get_all)
        self.bp.add_url_rule("/admin/lessons/<int:id>/", view_func=self.get_by_id)
        self.bp.add_url_rule("/admin/lessons/create/", view_func=self.create, methods=["POST", "GET"])

    def get_all(self):
        lessons = Lesson.query.all()
        return render_template("admin/lessons/index.html", lessons=lessons)

    def get_by_id(self, id):
        lesson = Lesson.query.get(id)
        return render_template("admin/lessons/view.html", lesson=lesson)

    def create(self):
        if request.method == "GET":
            return render_template("admin/lessons/create.html")
        else:
            title = request.form["title"]
            category = request.form["category"]
            level = request.form["level"]

            new_lesson = Lesson(title=title, category=category, level=level)
            db.session.add(new_lesson)
            db.session.commit()
            return redirect("/")

    def edit(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
