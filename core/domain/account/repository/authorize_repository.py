from abc import ABC, abstractmethod


class AuthorizeRepository(ABC):

    @abstractmethod
    def get_user(self):
        return NotImplemented
