from abc import ABC, abstractmethod

class IAccount(ABC):
    # attributes
    @property
    @abstractmethod
    def amount(self) -> float:
        pass

    @amount.setter
    def amount(self, value: float) -> None:
        pass