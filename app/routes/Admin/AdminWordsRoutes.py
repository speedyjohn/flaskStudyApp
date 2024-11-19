from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import WordForm
from app.forms.utils import fill_word_form
from app.models import Word, db, Lesson


class AdminWordRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp
        self.prefix = "/admin/words/"

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit)
        self.bp.add_url_rule(f"{self.prefix}update/", view_func=self.update, methods=["PUT"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        words = Word.query.all()
        return render_template(f"{self.prefix}index.html", words=words)

    def get(self, id):
        word = Word.query.get(id)
        return render_template(f"{self.prefix}view.html", word=word)

    def create(self):
        form = fill_word_form(WordForm())
        lessons = Lesson.query.all()
        many_rows = request.form.get("many_rows", False)
        if form.validate_on_submit():
            print(many_rows)
            lesson = request.form["lesson"]
            if not many_rows:
                word = request.form["word"]
                translation = request.form["translation"]

                row = Word(word=word, translation=translation, lesson_id=lesson)
                db.session.add(row)
            else:
                words = request.form["words"].split("\n")
                rows = []
                for row in words:
                    word, translation = row.split("-")
                    translation = translation.strip()

                    row = Word(word=word, translation=translation, lesson_id=lesson)
                    rows.append(row)

                db.session.add_all(rows)

            db.session.commit()
            return redirect(self.prefix)

        return render_template(f"{self.prefix}create.html", lessons=lessons, form=form)

    def insert(self):
        if request.form["many_lines"] == "on":
            words = request.form["words"].split("\n")
            word_rows = []
            for string in words:
                word, translation = string.split("-")
                translation = translation.strip()
                lesson = request.form["lesson"]

                new_word = Word(word=word, translation=translation, lesson_id=lesson)
                word_rows.append(new_word)
            db.session.add_all(word_rows)
            db.session.commit()
        else:
            word = request.form["word"]
            translation = request.form["translation"]
            lesson = request.form["lesson"]

            new_word = Word(word=word, translation=translation, lesson_id=lesson)
            db.session.add(new_word)
            db.session.commit()
        return redirect(self.prefix)

    def edit(self, id):
        word = Word.query.get(id)
        return render_template(f"{self.prefix}edit.html", word=word)

    def update(self):
        if request.method == "PUT":
            data = request.json
            id = data.get("id")
            word = Word.query.get(id)
            word.word = data.get("word")
            word.translation = data.get("translation")
            word.lesson_id = data.get("lesson")
            db.session.commit()
            return jsonify({"success": True}), 204

    def delete(self, id):
        if request.method == "DELETE":
            word = Word.query.get(id)
            db.session.delete(word)
            db.session.commit()
            return jsonify({"success": True}), 204
