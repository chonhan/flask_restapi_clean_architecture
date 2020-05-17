from abc import ABC, abstractmethod

from .port import UseCaseRequest, UseCaseResponse, UseCaseOutputPort


class UseCase(ABC):

    @abstractmethod
    def execute(self, uc_request: UseCaseRequest, uc_output_port: UseCaseOutputPort[UseCaseResponse]) -> None:
        return NotImplemented
