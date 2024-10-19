from flask import Flask

from app.blueprints import register_blueprints
from app.models import db
from app.utils import count_rows


def create_app():
    # Создаем экземпляр Flask с измененными путями к статике и шаблонам
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Настройка SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///db.db"

    register_blueprints(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.context_processor
    def inject_counts():
        counts = count_rows()
        return counts

    return app
