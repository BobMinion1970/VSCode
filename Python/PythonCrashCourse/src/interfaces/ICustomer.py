# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from abc import ABC, abstractmethod
from src.interfaces.IAccount import IAccount
class ICustomer(ABC):
    # attributes
    @property
    @abstractmethod
    def firstname(self) -> str: 
        pass
    @firstname.setter
    def firstname(self, value):
        pass
    
    @property
    @abstractmethod
    def lastname(self) -> str:
        pass 
    
    @lastname.setter
    def lastname(self, value):
        pass
    
    @property 
    @abstractmethod
    def account(self) -> IAccount:
        pass
    @account.setter
    def account(self, value: IAccount):
        pass
    
    # methods
    @abstractmethod
    def getFullName(self):
        pass