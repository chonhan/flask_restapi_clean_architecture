from flask_restplus import Resource

from apps.api.profile.controllers import search_api as api


@api.route('/member')
class MemberSearch(Resource):
    @api.doc('Search Member')
    def post(self):
        return ['search member']


@api.route('/newcomer')
class NewcomerSearch(Resource):
    @api.doc('Search Newcomer')
    def post(self):
        return ['search newcomer']
