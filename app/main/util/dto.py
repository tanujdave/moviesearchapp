from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class MovieDto:
    api = Namespace('movie', description='movie related operations')
    movie = api.model('movie', {
        'id' : fields.Integer(required=True, description='The movie id'),
        'name' : fields.String(required=True, description='The movie name'),
        'popularity' : fields.Float(required=True, description='The movie popularity'),
        'director' : fields.String(required=True, description='The movie director'),
        'imdb_score' : fields.Float(required=True, description='The movie imdb_score'),
        'genre' : fields.List(fields.String),
    })

class GenreDto:
    api = Namespace('genre', description='genre related operations')
    genre = api.model('genre', {
        'name' : fields.String(required=True, description='The genre name')
    })
