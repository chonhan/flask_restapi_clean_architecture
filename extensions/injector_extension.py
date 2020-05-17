from flask_injector import FlaskInjector
from injector import singleton, Binder

from core.domain.profile.repository.profile_repository import ProfileRepository
from core.domain.profile.use_case.get_user_profile import GetUserProfileUseCase
from infra.sql.profile.repository.sql_profile_repository import SqlProfileRepository
# from infra.mock.repository import MockProfileRepository


def configure_binding(binder: Binder) -> Binder:
    binder.bind(GetUserProfileUseCase, to=GetUserProfileUseCase, scope=singleton)
    # binder.bind(ProfileRepository, to=MockProfileRepository, scope=singleton)
    binder.bind(ProfileRepository, to=SqlProfileRepository, scope=singleton)
    return binder


def register_dependency_injection(app):
    FlaskInjector(app=app, modules=[configure_binding])
