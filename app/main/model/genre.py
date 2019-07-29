from .. import db
from sqlalchemy.orm import relationship


class Genre(db.Model):
    """ Genre model to store movie genre related data """
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name