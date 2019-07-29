from flask import request
from flask_restplus import Resource

from ..util.dto import GenreDto
from app.main.util.decorator import admin_token_required, token_required
from ..service.genre_service import save_new_genre, get_all_genre, get_a_genre

api = GenreDto.api
_genre = GenreDto.genre

parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/')
@api.expect(parser)
class GenreList(Resource):
    @api.doc('list_of_all_genres')
    @token_required
    @api.marshal_list_with(_genre, envelope='data')
    def get(self):
        """List all genres"""
        return get_all_genre()

    @api.expect(_genre, validate=True)
    @api.response(201, 'Genre successfully created.')
    @admin_token_required
    @api.doc('create a new genre')
    def post(self):
        """Creates a new Genre """
        data = request.json
        return save_new_genre(data=data)