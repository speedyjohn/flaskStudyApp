from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import CategoryForm
from app.models import db, Category


class AdminCategoryRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp
        self.prefix = "/admin/categories/"

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit, methods=["GET", "POST"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        categories = Category.query.all()
        return render_template(f"{self.prefix}index.html", categories=categories)

    def get(self, id):
        category = Category.query.get(id)
        return render_template(f"{self.prefix}view.html", category=category)

    def create(self):
        form = CategoryForm()
        if form.validate_on_submit():
            title = request.form["title"]

            category = Category(title=title)
            db.session.add(category)
            db.session.commit()
            return redirect(self.prefix)

        return render_template(f"{self.prefix}create.html", form=form)

    def edit(self, id):
        category = Category.query.get(id)
        form = CategoryForm()
        if form.validate_on_submit():
            category.title = request.form["title"]
            db.session.commit()
            return redirect(f"{self.prefix}{id}")

        return render_template(f"{self.prefix}edit.html", category=category, form=form)

    def update(self):
        if request.method == "PUT":
            data = request.json
            id = data.get("id")
            category = Category.query.get(id)
            category.title = data.get("title")
            db.session.commit()
            return jsonify({"success": True}), 204

    def delete(self, id):
        if request.method == "DELETE":
            category = Category.query.get(id)
            db.session.delete(category)
            db.session.commit()
            return jsonify({"success": True}), 204
