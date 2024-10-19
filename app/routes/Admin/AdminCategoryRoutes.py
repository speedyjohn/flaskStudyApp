from flask import Blueprint, render_template, request, redirect, jsonify

from app.models import db, Category


class AdminCategoryRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp
        self.prefix = "/admin/categories/"

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create)
        self.bp.add_url_rule(f"{self.prefix}insert/", view_func=self.insert, methods=["POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit)
        self.bp.add_url_rule(f"{self.prefix}update/", view_func=self.update, methods=["PUT"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        categories = Category.query.all()
        return render_template(f"{self.prefix}index.html", categories=categories)

    def get(self, id):
        category = Category.query.get(id)
        return render_template(f"{self.prefix}view.html", category=category)

    def create(self):
        return render_template(f"{self.prefix}create.html")

    def insert(self):
        title = request.form["title"]

        new_category = Category(title=title)
        db.session.add(new_category)
        db.session.commit()
        return redirect(self.prefix)

    def edit(self, id):
        category = Category.query.get(id)
        return render_template(f"{self.prefix}edit.html", category=category)

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
