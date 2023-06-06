# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from abc import ABC, abstractmethod, abstractproperty

class ICompany(ABC):
    
    @abstractmethod
    def add(self, other):
        pass
   
   