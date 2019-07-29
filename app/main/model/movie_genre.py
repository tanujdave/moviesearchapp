from .. import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey


class MovieGenre(db.Model):
    """ MovieGenre model to store movie genres data """
    __tablename__ = "movie_genre"

    movie_id = db.Column(db.Integer, ForeignKey('movie.id'), primary_key=True)
    genre_id = db.Column(db.Integer, ForeignKey('genre.id'), primary_key=True)
    movie = relationship("Movie")
    genre = relationship("Genre")

    def __init__(self, movie, genre):
        self.movie = movie
        self.genre = genre
    