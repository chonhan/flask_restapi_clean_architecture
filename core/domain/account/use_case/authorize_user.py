from core.kernel.use_case import UseCase
from core.kernel.port import UseCaseRequest, UseCasePresenter
from core.domain.account.repository.authorize_repository import AuthorizeRepository


class AuthorizeUser(UseCase):

    _auth_repo = None

    def __init__(self, auth_repo: AuthorizeRepository):
        self._auth_repo = auth_repo

    def execute(self, uc_request: UseCaseRequest, uc_presenter: UseCasePresenter) -> None:
        pass
