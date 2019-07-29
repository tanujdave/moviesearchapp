from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.movie_controller import api as movie_ns
from .main.controller.genre_controller import api as genre_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Fyndo - IMDB Movie search API',
          version='1.0'
        )

api.add_namespace(movie_ns, path='/movies')
api.add_namespace(genre_ns, path='/genres')
api.add_namespace(user_ns, path='/users')
api.add_namespace(auth_ns)