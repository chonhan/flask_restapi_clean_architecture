import attr
from injector import inject

from core.domain.profile.exception import UserNotFound
from core.domain.profile.repository.profile_repository import ProfileRepository
from core.kernel.port import UseCaseRequest, UseCaseResponse, UseCaseOutputPort
from core.kernel.use_case import UseCase


@attr.s(auto_attribs=True)
class GetUserProfileRequest(UseCaseRequest):
    user_id: int = None
    user_type: str = None


@attr.s(auto_attribs=True)
class GetUserProfileResponse(UseCaseResponse):
    """ Extends UseCase Response """


class GetUserProfileUseCase(UseCase):
    _profile_repo = None

    @inject
    def __init__(self, profile_repo: ProfileRepository):
        self._profile_repo = profile_repo

    def execute(self, uc_request: GetUserProfileRequest,
                uc_output_port: UseCaseOutputPort[GetUserProfileResponse]) -> None:
        response = GetUserProfileResponse()
        user = self._profile_repo.get_user(uc_request.user_type, uc_request.user_id)
        if not user:
            response.error = UserNotFound("This user does not exist")
        else:
            response.result = user
        uc_output_port.handle(response)
