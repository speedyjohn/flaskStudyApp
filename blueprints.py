from flask import Blueprint, Flask

from routes.Admin.AdminLessonRoutes import AdminLessonRoutes
from routes.Admin.AdminRoutes import AdminRoutes
from routes.Main.LessonRoutes import LessonRoutes
from routes.Main.MainRoutes import MainRoutes


def register_blueprints(app: Flask):
    admin_bp = Blueprint("admin", __name__)
    admin_lessons_bp = Blueprint("admin_lessons", __name__)

    main_bp = Blueprint("main", __name__)
    lesson_bp = Blueprint("lessons", __name__)

    admin_routes = AdminRoutes(admin_bp)
    admin_lesson_routes = AdminLessonRoutes(admin_lessons_bp)

    main_routes = MainRoutes(main_bp)
    lesson_routes = LessonRoutes(lesson_bp)

    app.register_blueprint(admin_routes.bp)
    app.register_blueprint(admin_lesson_routes.bp)

    app.register_blueprint(main_routes.bp)
    app.register_blueprint(lesson_routes.bp)

