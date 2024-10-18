from flask import Blueprint, render_template, request, redirect, jsonify

from models import Lesson, db


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
        return render_template("admin/lessons/index.html", lessons=lessons)

    def get(self, id):
        lesson = Lesson.query.get(id)
        return render_template("admin/lessons/view.html", lesson=lesson)

    def create(self):
        return render_template("admin/lessons/create.html")

    def insert(self):
        title = request.form["title"]
        category = request.form["category"]
        level = request.form["level"]

        new_lesson = Lesson(title=title, category=category, level=level)
        db.session.add(new_lesson)
        db.session.commit()
        return redirect("/")

    def edit(self, id):
        lesson = Lesson.query.get(id)
        return render_template("admin/lessons/edit.html", lesson=lesson)

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
