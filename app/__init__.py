from flask import Flask

from app.blueprints import register_blueprints
from app.models import db
from app.utils import count_rows


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///db.db"
    app.config["SECRET_KEY"] = "veryhardsecretkey"

    register_blueprints(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.context_processor
    def inject_counts():
        counts = count_rows()
        return counts

    return app
