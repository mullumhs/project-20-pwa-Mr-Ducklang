from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(100), nullable=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable = True)

    def __repr__(self):
        return f'<Task {self.Title}>'