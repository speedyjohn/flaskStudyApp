from abc import ABC, abstractmethod

from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import CategoryForm, BaseForm
from app.models import db, Category


class AdminCRUDRoutes:
    def __init__(self, bp: Blueprint, prefix: str, model: db.Model, form: BaseForm):
        self.bp = bp
        self.prefix = prefix
        self.model = model
        self.form = form

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        rows = self.model.query.all()
        return rows

    def get(self, id):
        row = self.model.query.get(id)
        return render_template(f"{self.prefix}view.html", row=row)

    def create(self, fill_func: None):
        if fill_func is not None and callable(fill_func):
            form = fill_func(self.form)
        else:
            form = self.form

        if form.validate_on_submit():
            params = {key: value for key, value in list(request.form.items())[1:-1]}

            row = self.model(**params)
            db.session.add(row)
            db.session.commit()
            return redirect(self.prefix)
        else:
            print(form.errors)

        return render_template(f"{self.prefix}create.html", form=form)

    def edit(self, id, fill_func: None):
        row = self.model.query.get(id)
        if fill_func is not None and callable(fill_func):
            form = fill_func(self.form)
        else:
            form = CategoryForm()

        if form.validate_on_submit():
            params = {key: value for key, value in list(request.form.items())[1:-1]}
            for key, value in params.items():
                if hasattr(row, key):
                    setattr(row, key, value)
            db.session.commit()
            return redirect(f"{self.prefix}{id}")
        else:
            print(form.errors)

        return render_template(f"{self.prefix}edit.html", row=row, form=form)

    def delete(self, id):
        if request.method == "DELETE":
            row = self.model.query.get(id)
            db.session.delete(row)
            db.session.commit()
            return jsonify({"success": True}), 204
