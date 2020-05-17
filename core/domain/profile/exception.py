import attr

from core.kernel.exception import BaseNotFoundException


@attr.s(auto_attribs=True)
class UserNotFound(BaseNotFoundException):
    """ User Not Found Exception """
    message: str = "User Not Found"
