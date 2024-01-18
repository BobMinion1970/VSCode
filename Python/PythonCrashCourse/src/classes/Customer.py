# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from src.interfaces.ICustomer import ICustomer
from src.interfaces.IAccount import IAccount

class Customer(ICustomer):
    
    def __init__(self, firstname : str ="", lastname : str ="", account: IAccount =None) -> None:
        self._firstname = firstname
        self._lastname = lastname
        self._account = account
    
    def getFullName(self) -> str:
        return self._firstname + " " + self._lastname
    
    def AddMoneyToAccount(self, amount: float) -> float:
       self.account.amount += amount
       return self.account.amount
    
    def RemoveMoneyFromAccount(self, amount: float) -> float:
        if self.account.amount - amount > 0:
            self.account.amount -= amount
        else: 
            raise ArithmeticError("Credit is less than the required amount")
        
        return self.account.amount - amount
            
    
    @property
    def lastname(self) -> str:
        return self._lastname
    @lastname.setter
    def lastname(self, value: str) -> None:
        self._lastname = value
        
    @property
    def firstname(self) -> str:
        return self._firstname
    @firstname.setter
    def firstname(self, value: str) -> None:
        self._firstname = value 
        
    @property
    def account(self) -> IAccount:
        return self._account
    @account.setter
    def account(self, account: IAccount):
        self._account = account 

