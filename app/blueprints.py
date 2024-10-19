from flask import Blueprint, Flask

from app.routes.Admin.AdminCategoryRoutes import AdminCategoryRoutes
from app.routes.Admin.AdminLevelRoutes import AdminLevelRoutes
from app.routes.Admin.AdminLessonRoutes import AdminLessonRoutes
from app.routes.Admin.AdminRoutes import AdminRoutes
from app.routes.Main.LessonRoutes import LessonRoutes
from app.routes.Main.MainRoutes import MainRoutes


def register_blueprints(app: Flask):
    admin_bp = Blueprint("admin", __name__)
    admin_lessons_bp = Blueprint("admin_lessons", __name__)
    admin_categories_bp = Blueprint("admin_categories", __name__)
    admin_levels_bp = Blueprint("admin_levels", __name__)

    main_bp = Blueprint("main", __name__)
    lesson_bp = Blueprint("lessons", __name__)

    admin_routes = AdminRoutes(admin_bp)
    admin_lesson_routes = AdminLessonRoutes(admin_lessons_bp)
    admin_categories_routes = AdminCategoryRoutes(admin_categories_bp)
    admin_levels_routes = AdminLevelRoutes(admin_levels_bp)

    main_routes = MainRoutes(main_bp)
    lesson_routes = LessonRoutes(lesson_bp)

    app.register_blueprint(admin_routes.bp)
    app.register_blueprint(admin_lesson_routes.bp)
    app.register_blueprint(admin_categories_routes.bp)
    app.register_blueprint(admin_levels_routes.bp)

    app.register_blueprint(main_routes.bp)
    app.register_blueprint(lesson_routes.bp)

