from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import LessonForm
from app.forms.utils import fill_lesson_form, fill_lesson_form_edit
from app.models import Lesson, db, Category, Level


class AdminLessonRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp
        self.prefix = "/admin/lessons/"

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        lessons = Lesson.query.all()
        return render_template(f"{self.prefix}index.html", lessons=lessons)

    def get(self, id):
        lesson = Lesson.query.get(id)
        return render_template(f"{self.prefix}view.html", lesson=lesson)

    def create(self):
        form = fill_lesson_form(LessonForm())
        if form.validate_on_submit():
            title = request.form["title"]
            category = request.form["category"]
            level = request.form["level"]

            lesson = Lesson(title=title, category_id=category, level_id=level)
            db.session.add(lesson)
            db.session.commit()
            return redirect(self.prefix)

        return render_template(f"{self.prefix}create.html", form=form)

    def edit(self, id):
        lesson = Lesson.query.get(id)
        form = fill_lesson_form_edit(LessonForm(), lesson)
        print(form.category.choices)
        if form.validate_on_submit():
            lesson.title = request.form["title"]
            lesson.category_id = request.form["category"]
            lesson.level_id = request.form["level"]
            db.session.commit()
            return redirect(f"{self.prefix}{id}/")
        categories = Category.query.all()
        levels = Level.query.all()
        return render_template(f"{self.prefix}edit.html", lesson=lesson, categories=categories, levels=levels, form=form)

    def delete(self, id):
        if request.method == "DELETE":
            lesson = Lesson.query.get(id)
            db.session.delete(lesson)
            db.session.commit()
            return jsonify({"success": True}), 204
