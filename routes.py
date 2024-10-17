# from flask import Blueprint, render_template, request, redirect
#
# from models import Lesson, db
#
# main = Blueprint("main", __name__)
#
#
# @main.route("/")
# @main.route("/index")
# def index():
#     return render_template("index.html")
#
#
# @main.route("/lessons/<int:id>")
# def lesson_by_id(id: int):
#     lesson = Lesson.query.get(id)
#     print(lesson)
#     return render_template("lessons/single.html", lesson=lesson)
#
#
# @main.route("/admin/lesson/create", methods=["POST", "GET"])
# def lesson_create():
#     if request.method == "GET":
#         return render_template("admin/lessons/create.html")
#     else:
#         title = request.form["title"]
#         category = request.form["category"]
#         level = request.form["level"]
#
#         new_lesson = Lesson(title=title, category=category, level=level)
#         db.session.add(new_lesson)
#         db.session.commit()
#         return redirect("/")
#
# @main.route("/lessons")
# def get_lessons():
#     lessons = Lesson.query.all()
#     return render_template("lessons/index.html", lessons=lessons)
