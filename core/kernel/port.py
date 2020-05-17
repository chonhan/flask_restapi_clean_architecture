from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Any

import attr
import cattr

from .exception import UseCaseException

T = TypeVar('T')


@attr.s(auto_attribs=True)
class UseCaseRequest(ABC):
    """ Base UseCase Request """


@attr.s(auto_attribs=True)
class UseCaseResponse(object):
    result: Any = None
    error: UseCaseException = None

    @property
    def is_succeeded(self):
        return self.error is None or self.result is not None


class UseCaseOutputPort(Generic[T]):

    def __str__(self):
        return f'{__class__.__name__} with Type: {T}'

    @abstractmethod
    def handle(self, response: T) -> None:
        return NotImplemented


class JsonContentResult(object):
    __content_result: Dict = {}

    def __init__(self, content: UseCaseResponse = None) -> None:
        if content and content.is_succeeded:
            self.__content_result = cattr.unstructure(content.result)

    @property
    def content_result(self) -> Dict:
        return self.__content_result

    @content_result.setter
    def content_result(self, content: UseCaseResponse) -> None:
        if content and content.is_succeeded:
            self.__content_result = cattr.unstructure(content.result)
