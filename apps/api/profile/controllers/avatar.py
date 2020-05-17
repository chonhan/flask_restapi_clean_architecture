from flask_restplus import Resource

from apps.api.profile.controllers import avatar_api as api


@api.route('/')
class AvatarList(Resource):
    @api.doc('Upload Avatar Image')
    def post(self):
        return ['avatar_post']


@api.route('/<string:avatar_id>')
class Avatar(Resource):
    @api.doc('Get Avatar Image')
    def get(self, avatar_id: str):
        return [avatar_id]
