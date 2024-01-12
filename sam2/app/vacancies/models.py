from .. import db, login_manager
from datetime import datetime

class Vacancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    qualification_level = db.Column(db.String(50), nullable=False)

    def __init__(self, title, description, qualification_level):
        self.title = title
        self.description = description
        self.qualification_level = qualification_level
