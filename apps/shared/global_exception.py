from werkzeug.exceptions import (
    HTTPException,
    BadRequest,
    NotFound
)


class CustomError(HTTPException):
    """ Custom Error Exception """
    code = 409
    description = "custom error"


class BadRequestError(BadRequest):
    """ Wrap BadRequest Exception """


class NotFoundError(NotFound):
    """ Wrap NotFound Exception """
