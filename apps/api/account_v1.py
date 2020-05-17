from flask import Blueprint
from flask_restplus import Api
from werkzeug.exceptions import HTTPException

from .account.controllers.security import api as security_api

blueprint = Blueprint('account_api', __name__, url_prefix='/account/v1')

api = Api(blueprint,
          doc='/doc/',
          title='Resource API - Account',
          version='1.0',
          description='A description'
          )

api.add_namespace(security_api)


@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """ Handle BluePrint JSON Error Response """
    response = {
        'error': error.__class__.__name__,
        'message': error.description,
    }
    return response, error.code
