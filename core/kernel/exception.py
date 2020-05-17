import attr


@attr.s(auto_attribs=True)
class UseCaseException(Exception):
    """ Base UseCase Error """
    message: str = None


@attr.s(auto_attribs=True)
class BaseNotFoundException(UseCaseException):
    """ Base Not Found Exception Abstraction """
