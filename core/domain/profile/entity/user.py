import attr
from typing import List

from core.kernel.entity import Entity
from .profile import UserBasicProfile, UserExtraProfile


@attr.s(auto_attribs=True)
class User(Entity):
    """ Base User Entity """
    user_type: str = None
    user_name: str = None
    user_status: str = "enabled"
    basic_profile: UserBasicProfile = None
    extra_profile: List[UserExtraProfile] = []


@attr.s(auto_attribs=True)
class Member(User):
    """ Member Entity Extends User """
    user_type: str = attr.ib(default="member", init=False)


@attr.s(auto_attribs=True)
class Newcomer(User):
    """ Newcomer Entity Extends User """
    user_type: str = attr.ib(default="newcomer", init=False)
