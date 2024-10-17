from flask import Flask

from models import db
from blueprints import register_blueprints

app = Flask(__name__)
register_blueprints(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
