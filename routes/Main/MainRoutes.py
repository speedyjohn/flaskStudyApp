from flask import Blueprint, render_template


class MainRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp

        self.bp.add_url_rule("/", view_func=self.index)

    def index(self):
        return render_template("index.html")
