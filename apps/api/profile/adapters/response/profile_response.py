from flask_restplus import fields

from apps.api.profile.controllers import member_api

entity = member_api.model('Entity', {
    'id': fields.Integer
})

basic_profile = member_api.model('BasicProfile', {
    'real_name': fields.String,
    'gender': fields.String,
    # 'birthday': fields.String
})

extra_profile = member_api.model('ExtraProfile', {
    'profile_category': fields.String,
    '*': fields.Wildcard(fields.String)
})

user_profile = member_api.clone('UserProfile', entity, {
    'user_type': fields.String,
    'user_name': fields.String,
    'user_status': fields.String,
})

member_profile = member_api.clone('MemberProfile', user_profile, {
    'basic_profile': fields.Nested(basic_profile),
    'extra_profile': fields.List(fields.Nested(extra_profile))
})

