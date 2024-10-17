from flask import Blueprint, Flask

from routes.Main.LessonRoutes import LessonRoutes
from routes.Main.MainRoutes import MainRoutes


def register_blueprints(app: Flask):
    main_bp = Blueprint("main", __name__)
    lesson_bp = Blueprint("lessons", __name__)

    main_routes = MainRoutes(main_bp)
    lesson_routes = LessonRoutes(lesson_bp)

    app.register_blueprint(main_routes.bp)
    app.register_blueprint(lesson_routes.bp)

