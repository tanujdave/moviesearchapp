from flask import request
from flask_restplus import Resource

from ..util.dto import MovieDto
from app.main.util.decorator import admin_token_required, token_required
from ..service.movie_service import save_new_movie, get_all_movies, get_a_movie, update_movie, search_movie, remove_movie

api = MovieDto.api
_movie = MovieDto.movie

parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/search')
@api.response(404, 'Movie not found.')
@api.expect(parser)
class MovieSearch(Resource):
    @api.doc('search_movies')
    @api.expect(_movie, validate=False)
    @token_required
    @api.marshal_list_with(_movie, envelope='data')
    def post(self):
        """Search movies"""
        data = request.json
        return search_movie(data=data)


@api.route('/')
@api.expect(parser)
class MovieList(Resource):

    @api.doc('list_of_all_movies')
    # @token_required
    @api.marshal_list_with(_movie, envelope='data')
    def get(self):
        """List all movies"""
        return get_all_movies()

    @api.expect(_movie, validate=True)
    @api.response(201, 'Movie successfully created.')
    @admin_token_required
    @api.doc('create a new movie')
    def post(self):
        """Creates a new Movie """
        data = request.json
        return save_new_movie(data=data)

    @api.expect(_movie, validate=True)
    @api.response(204, 'Movie successfully updated.')
    @admin_token_required
    @api.doc('update movie')
    def put(self):
        """Update Movie """
        data = request.json
        return update_movie(data=data)


@api.route('/<id>')
@api.param('id', 'The User id')
@api.response(404, 'Movie not found.')
@api.expect(parser)
class Movie(Resource):
    @api.doc('get a movie')
    @token_required
    @api.marshal_with(_movie)
    def get(self, id):
        """get a movie given its id"""
        movie = get_a_movie(id)
        if not movie:
            api.abort(404)
        else:
            return movie

    @api.doc('remove a movie')
    @admin_token_required
    @api.marshal_with(_movie)
    def delete(self, id):
        """remove a movie given its id"""
        return remove_movie(id)