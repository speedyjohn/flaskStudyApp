from flask import Blueprint, render_template, request, redirect, jsonify

from app.models import Lesson, db, Category, Level
from app.utils import count_rows


class AdminLessonRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp
        self.prefix = "/admin/lessons/"

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create)
        self.bp.add_url_rule(f"{self.prefix}insert/", view_func=self.insert, methods=["POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit)
        self.bp.add_url_rule(f"{self.prefix}update/", view_func=self.update, methods=["PUT"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        lessons = Lesson.query.all()
        return render_template(f"{self.prefix}index.html", lessons=lessons)

    def get(self, id):
        lesson = Lesson.query.get(id)
        return render_template(f"{self.prefix}view.html", lesson=lesson)

    def create(self):
        categories = Category.query.all()
        levels = Level.query.all()
        return render_template(f"{self.prefix}create.html", categories=categories, levels=levels)

    def insert(self):
        title = request.form["title"]
        category = request.form["category"]
        level = request.form["level"]

        new_lesson = Lesson(title=title, category_id=category, level_id=level)
        db.session.add(new_lesson)
        db.session.commit()
        return redirect(self.prefix)

    def edit(self, id):
        lesson = Lesson.query.get(id)
        return render_template(f"{self.prefix}edit.html", lesson=lesson)

    def update(self):
        if request.method == "PUT":
            data = request.json
            id = data.get("id")
            lesson = Lesson.query.get(id)
            lesson.title = data.get("title")
            lesson.category = data.get("category")
            lesson.level = data.get("level")
            db.session.commit()
            print(data)
            return jsonify({"success": True}), 204

    def delete(self, id):
        if request.method == "DELETE":
            lesson = Lesson.query.get(id)
            db.session.delete(lesson)
            db.session.commit()
            return jsonify({"success": True}), 204
