from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quote = db.Column(db.String(100), nullable = True)
    description = db.Column(db.Text)
    owner = db.Column(db.String(100), nullable = True)
    type = db.Column(db.String(100), nullable=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable = True)
    issues = db.Column(db.Text)

    def __repr__(self):
        return f'<Task {self.Title}>'