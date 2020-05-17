from flask_restplus import fields

from apps.api.profile.controllers import member_api

member_id_request = member_api.model('MemberIdRequest', {
    'id': fields.Integer
})
