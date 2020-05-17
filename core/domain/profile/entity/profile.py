import attr
from datetime import date

from core.kernel.entity import ValueObject


@attr.s(auto_attribs=True)
class UserBasicProfile(ValueObject):
    """ User Basic Profile """
    real_name: str = None
    gender: str = None
    birthday: str = None


@attr.s(auto_attribs=True)
class UserExtraProfile(ValueObject):
    """ Base User Extra Profile """
    profile_category: str = None


@attr.s(auto_attribs=True)
class EducationExtraProfile(UserExtraProfile):
    """ Education Extra Profile """
    profile_category: str = attr.ib(default="education", init=False)
    school: str = None
    department: str = None


@attr.s(auto_attribs=True)
class CareerExtraProfile(UserExtraProfile):
    """ Career Extra Profile """
    profile_category: str = attr.ib(default="career", init=False)
    career: str = None
    job_title: str = None
