from flask import Blueprint, render_template


class AdminRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp

        self.bp.add_url_rule("/admin/", view_func=self.index)

    def index(self):
        return render_template("admin/index.html")
