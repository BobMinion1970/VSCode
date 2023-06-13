# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from abc import ABC, abstractmethod

class IBow(ABC):
    @property           # property strength
    @abstractmethod
    def strength(self) -> str:
        raise NotImplementedError
    
    @strength.setter
    @abstractmethod
    def strength(self, value: str) -> None:
        raise NotImplementedError
   
    @property           # property material
    @abstractmethod
    def material(self) -> str:
        raise NotImplementedError
    
    @material.setter
    @abstractmethod
    def material(self, value: str) -> None:
        raise NotImplementedError