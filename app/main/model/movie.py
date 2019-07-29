from .. import db
from sqlalchemy.orm import relationship


class Movie(db.Model):
    """ Movie model to store movie related data """
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    popularity = db.Column(db.Float(), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    imdb_score = db.Column(db.Float(), nullable=False)
    genres = relationship("MovieGenre")
