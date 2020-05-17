from flask_restplus import Resource
from injector import inject

from apps.api.profile.adapters.presenters.profile_presenter import GetUserProfilePresenter
from apps.api.profile.adapters.response.profile_response import member_profile
from apps.api.profile.controllers import member_api as api
from apps.shared.global_exception import CustomError, BadRequestError, NotFoundError
from core.domain.profile.use_case.get_user_profile import GetUserProfileUseCase, GetUserProfileRequest


@api.route('/')
class MemberList(Resource):
    @api.doc('Create Member')
    @api.response(400, 'Bad Request')
    def post(self):
        return ['create member']


@api.route('/<int:member_id>/')
class Member(Resource):

    @inject
    def __init__(self, uc_get_profile: GetUserProfileUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._uc_get_profile = uc_get_profile

    @api.doc('Get Member')
    @api.response(404, 'User Not Found')
    @api.marshal_with(member_profile)
    def get(self, member_id: int):
        uc_request = GetUserProfileRequest(member_id, "member")
        presenter = GetUserProfilePresenter()
        self._uc_get_profile.execute(uc_request, presenter)
        return presenter.content_result


@api.route('/<int:member_id>/basic')
class MemberBasic(Resource):
    @api.doc('Get Member Basic info')
    @api.response(404, 'User Not Found')
    def put(self, member_id: int):
        # return ['put member basic']
        raise CustomError('Bad key123')


@api.route('/<int:member_id>/extra')
class MemberExtra(Resource):
    @api.doc('Get Member Extra Info')
    @api.response(404, 'User Not Found')
    def put(self, member_id: int):
        # return ['put member extra']
        raise BadRequestError('wrong parameter abc')
