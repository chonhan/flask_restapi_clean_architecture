from flask import Blueprint
from flask_restplus import Api
from werkzeug.exceptions import HTTPException

from .profile.controllers.avatar import api as avatar_api
from .profile.controllers.member import api as member_api
from .profile.controllers.search import api as search_api

blueprint = Blueprint('profile_api', __name__, url_prefix='/profile/v1')

api = Api(blueprint,
          doc='/doc/',
          title='Resource API - Profile',
          version='1.0',
          description='A description'
          )

api.add_namespace(avatar_api)
api.add_namespace(search_api)
api.add_namespace(member_api)


@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """ Handle BluePrint JSON Error Response """
    response = {
        'error': error.__class__.__name__,
        'message': error.description,
    }
    return response, error.code
