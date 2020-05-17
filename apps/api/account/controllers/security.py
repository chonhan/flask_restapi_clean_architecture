from flask_restplus import Namespace, Resource

from extensions.log_extension import get_logger

api = Namespace('security', description='Security Endpoints')
logger = get_logger(__name__)


@api.route('/authorize')
class Authorize(Resource):
    @api.doc('Authorize Requests')
    def get(self):
        logger.info('authorize')
        return ['authorize']


@api.route('/logout')
class Logout(Resource):
    @api.doc('Logout Endpoint')
    def get(self):
        logger.warn('logout')
        return {'logout': True}


@api.route('/inquiry')
class Inquiry(Resource):
    @api.doc('Query Account')
    def get(self):
        logger.debug('inquiry')
        return ['Query']


@api.route('/token')
class Token(Resource):
    @api.doc('Exchange Tokens')
    def get(self):
        logger.info('token')
        return ['Token']
