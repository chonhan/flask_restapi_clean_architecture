from typing import List

from core.domain.profile.entity.profile import (
    UserBasicProfile, EducationExtraProfile, CareerExtraProfile, UserExtraProfile
)
from core.domain.profile.entity.user import User, Member, Newcomer
from core.domain.profile.exception import UserNotFound
from core.domain.profile.repository.profile_repository import ProfileRepository


class MockProfileRepository(ProfileRepository):
    _users: List[User] = []

    def __init__(self):
        education_profile = EducationExtraProfile(school="College", department="Art")
        career_profile = CareerExtraProfile(career="Developer", job_title="Sr. Developer II")
        member = Member(
            id=111,
            user_name="Mock",
            user_status="enabled",
            basic_profile=UserBasicProfile(real_name="Hello Mock", gender="Male", birthday=""),
            extra_profile=[education_profile, career_profile]
        )
        newcomer = Newcomer(
            id=112,
            user_name="Nancy",
            user_status="enabled",
            basic_profile=UserBasicProfile(real_name="Hello Nancy", gender="Female", birthday=""),
            extra_profile=[career_profile]
        )
        self._users.append(member)
        self._users.append(newcomer)

    def get_user(self, user_type: str, user_id: int) -> User:
        user = next((x for x in self._users if x.id == user_id and x.user_type == user_type), None)
        return user

    def create_user(self, user: User) -> None:
        self._users.append(user)

    def update_user_basic(self, user_type: str, user_id: int, basic_profile: UserBasicProfile) -> None:
        user = next((x for x in self._users if x.id == user_id and x.user_type == user_type), None)
        if user:
            user.basic_profile = basic_profile
        else:
            raise UserNotFound()

    def update_user_extra(self, user_type: str, user_id: int, extra_profiles: List[UserExtraProfile]) -> None:
        user = next((x for x in self._users if x.id == user_id and x.user_type == user_type), None)
        if user:
            user.extra_profile = extra_profiles
        else:
            raise UserNotFound()
