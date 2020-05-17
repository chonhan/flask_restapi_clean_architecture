from abc import ABC, abstractmethod
from typing import List

from core.domain.profile.entity.user import User, UserBasicProfile, UserExtraProfile


class ProfileRepository(ABC):

    @abstractmethod
    def get_user(self, user_type: str, user_id: int) -> User:
        return NotImplemented

    @abstractmethod
    def create_user(self, user: User) -> None:
        return NotImplemented

    @abstractmethod
    def update_user_basic(self, user_type: str, user_id: int, basic_profile: UserBasicProfile) -> None:
        return NotImplemented

    @abstractmethod
    def update_user_extra(self, user_type: str, user_id: int, extra_profiles: List[UserExtraProfile]) -> None:
        return NotImplemented
