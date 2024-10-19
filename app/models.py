from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)

    category = db.relationship('Category', backref=db.backref('lessons', lazy=True))
    level = db.relationship('Level', backref=db.backref('lessons', lazy=True))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)


class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    indicator = db.Column(db.Integer)

