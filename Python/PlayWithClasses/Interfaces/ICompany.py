# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from abc import ABC, abstractmethod

class ICompany(ABC):
    
    @abstractmethod
    def add(self, other):
        pass
    
    @property
    @abstractmethod
    def actualcount(self) -> int: 
        raise NotImplementedError
        
   