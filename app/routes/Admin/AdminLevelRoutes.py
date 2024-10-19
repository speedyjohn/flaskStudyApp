from flask import Blueprint, render_template, request, redirect, jsonify

from app.models import Level, db


class AdminLevelRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp
        self.prefix = "/admin/levels/"

        self.bp.add_url_rule(f"{self.prefix}", view_func=self.get_all)
        self.bp.add_url_rule(f"{self.prefix}<int:id>/", view_func=self.get)
        self.bp.add_url_rule(f"{self.prefix}create/", view_func=self.create)
        self.bp.add_url_rule(f"{self.prefix}insert/", view_func=self.insert, methods=["POST"])
        self.bp.add_url_rule(f"{self.prefix}edit/<int:id>", view_func=self.edit)
        self.bp.add_url_rule(f"{self.prefix}update/", view_func=self.update, methods=["PUT"])
        self.bp.add_url_rule(f"{self.prefix}delete/<int:id>", view_func=self.delete, methods=["DELETE"])

    def get_all(self):
        levels = Level.query.all()
        return render_template(f"{self.prefix}index.html", levels=levels)

    def get(self, id):
        level = Level.query.get(id)
        return render_template(f"{self.prefix}view.html", level=level)

    def create(self):
        return render_template(f"{self.prefix}create.html")

    def insert(self):
        title = request.form["title"]
        indicator = request.form["indicator"]

        new_level = Level(title=title, indicator=indicator)
        db.session.add(new_level)
        db.session.commit()
        return redirect(self.prefix)

    def edit(self, id):
        level = Level.query.get(id)
        return render_template(f"{self.prefix}edit.html", level=level)

    def update(self):
        if request.method == "PUT":
            data = request.json
            id = data.get("id")
            level = Level.query.get(id)
            level.title = data.get("title")
            level.indicator = data.get("indicator")
            db.session.commit()
            print(data)
            return jsonify({"success": True}), 204

    def delete(self, id):
        if request.method == "DELETE":
            level = Level.query.get(id)
            db.session.delete(level)
            db.session.commit()
            return jsonify({"success": True}), 204
