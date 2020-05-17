from apps.shared.global_exception import NotFoundError

from core.domain.profile.use_case.get_user_profile import GetUserProfileResponse
from core.kernel.exception import BaseNotFoundException
from core.kernel.port import JsonContentResult
from core.kernel.use_case import UseCaseOutputPort


class GetUserProfilePresenter(UseCaseOutputPort[GetUserProfileResponse], JsonContentResult):

    def handle(self, response: GetUserProfileResponse) -> None:
        if not response.is_succeeded:
            if isinstance(response.error, BaseNotFoundException):
                raise NotFoundError(response.error.message)
        self.content_result = response
