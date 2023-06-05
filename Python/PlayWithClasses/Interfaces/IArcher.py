# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from abc import ABC, abstractmethod

class IArcher(ABC):
    @abstractmethod
    def shoot(self):
        pass
        
    @abstractmethod
    def increase_arrows(self, new_arrows:int):
        pass
        