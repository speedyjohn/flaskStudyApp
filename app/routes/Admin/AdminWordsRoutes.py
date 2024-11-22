from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import WordForm
from app.forms.utils import fill_word_form, fill_word_form_edit
from app.models import Word, db, Lesson
from app.routes.Admin.AdminCRUDRoutes import AdminCRUDRoutes


class AdminWordRoutes(AdminCRUDRoutes):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, "/admin/words/", Word, WordForm)

    def create(self):
        form = fill_word_form(WordForm())
        rows = Lesson.query.all()
        many_rows = request.form.get("many_rows", False)
        if form.validate_on_submit():
            lesson = request.form["lesson_id"]
            if not many_rows:
                word = request.form["word"]
                translation = request.form["translation"]

                row = Word(word=word, translation=translation, lesson_id=lesson)
                db.session.add(row)
            else:
                words = request.form["words"].split("\n")
                new_rows = []
                for row in words:
                    word, translation = row.split("-")
                    translation = translation.strip()

                    row = Word(word=word, translation=translation, lesson_id=lesson)
                    new_rows.append(row)

                db.session.add_all(new_rows)

            db.session.commit()
            return redirect(self.prefix)

        return render_template(f"{self.prefix}create.html", rows=rows, form=form)

    def edit(self, id):
        response = super().edit(id, fill_word_form_edit)
        return response