# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from src.interfaces.ICustomer import ICustomer
from src.interfaces.IAccount import IAccount

class Customer(ICustomer):
    
    def __init__(self, customerid : int = 0, firstname : str ="", lastname : str ="", account: IAccount =None) -> None:
        self._customerid = customerid 
        self._firstname = firstname
        self._lastname = lastname
        self._account = account
    
    def getFullName(self) -> str:
        return self._firstname + " " + self._lastname
    
    def getFullNameWithID() -> str:
        pass 
    
    def AddMoneyToAccount(self, amount: float) -> float:
        if amount >= 0:
            self.account.credit += amount     
        else:
            raise ArithmeticError("Amount is negative")
    
    def RemoveMoneyFromAccount(self, amount: float) -> float:
        if self.account.credit - amount > 0:
            self.account.credit -= amount
        else: 
            raise ArithmeticError("Credit is less than the required amount")
        
        return self.account.credit - amount
            
    @property
    def customerid(self) -> int:
        return self._customerid
    
    @customerid.setter
    def customerid(self, value) -> None:
        self._customerid = value
    
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

