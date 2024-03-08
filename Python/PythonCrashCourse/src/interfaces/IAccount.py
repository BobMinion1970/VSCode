from abc import ABC, abstractmethod

class IAccount(ABC):
    # attributes
    @property
    @abstractmethod
    def credit(self) -> float:
        pass
    @credit.setter
    def credit(self, value: float) -> None:
        pass