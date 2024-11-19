from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import LevelForm
from app.models import Level, db


class AdminLevelRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp
        self.prefix = "/admin/levels/"

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        levels = Level.query.all()
        return render_template(f"{self.prefix}index.html", levels=levels)

    def get(self, id):
        level = Level.query.get(id)
        return render_template(f"{self.prefix}view.html", level=level)

    def create(self):
        form = LevelForm()
        if form.validate_on_submit():
            title = request.form["title"]
            indicator = request.form["indicator"]
            level = Level(title=title, indicator=indicator)
            db.session.add(level)
            db.session.commit()
            return redirect(self.prefix)

        return render_template(f"{self.prefix}create.html", form=form)

    def edit(self, id):
        level = Level.query.get(id)
        form = LevelForm()
        if form.validate_on_submit():
            level.title = request.form["title"]
            level.indicator = request.form["indicator"]
            db.session.commit()
            return redirect(f"{self.prefix}{id}")
        return render_template(f"{self.prefix}edit.html", level=level, form=form)


    def delete(self, id):
        if request.method == "DELETE":
            level = Level.query.get(id)
            db.session.delete(level)
            db.session.commit()
            return jsonify({"success": True}), 204
