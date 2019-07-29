from app.main import db
from app.main.model.movie import Movie
from app.main.model.genre import Genre
from app.main.model.movie_genre import MovieGenre
from sqlalchemy.orm import lazyload, joinedload

def search_movie(data):
    query = Movie.query

    for field, value in data.items():
        if value and 'genre' != field:
            query = query.filter(getattr(Movie, field)==value)
    
    return query.all()

def update_movie(data):
    if not data['id']:
        response_object = {
            'status': 'error',
            'message': 'movie id missing.'
        }
        return response_object, 404

    movie = Movie.query.filter_by(id=data['id']).first()
    if not movie:
        response_object = {
            'status': 'error',
            'message': 'movie not found.'
        }
        return response_object, 404

    
    movie.name = data['name']
    movie.popularity = data['popularity']
    movie.director = data['director']
    movie.imdb_score = data['imdb_score']

    save_changes(movie)
    response_object = {
        'status': 'success',
        'message': 'Successfully updated.'
    }
    return response_object, 204

def save_new_movie(data):
    new_movie = Movie(
            name=data['name'],
            popularity=data['popularity'],
            director=data['director'],
            imdb_score=data['imdb_score']
        )
    for genre in data['genre']:
        saved_genre = Genre.query.filter_by(name=genre).first()
        if saved_genre:
            new_movie.genres.append(MovieGenre(new_movie, saved_genre))
        else:
            new_genre = Genre(name=genre)
            new_movie.genres.append(MovieGenre(new_movie, new_genre))

    save_changes(new_movie)
    response_object = {
        'status': 'success',
        'message': 'Successfully created.'
    }
    return response_object, 201


def get_all_movies():
    return Movie.query.all()


def get_a_movie(id):
    return Movie.query.filter_by(id=id).first()


def remove_movie(id):
    movie = get_a_movie(id)
    if not movie:
        response_object = {
            'status': 'failed',
            'message': 'movie not found.'
        }
        return response_object, 404

    db.session.remove(movie)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'movie delet successfully.'
    }
    return response_object, 204


def save_changes(data):
    db.session.add(data)
    db.session.commit()