from src.interfaces.IAccount import IAccount

class Account(IAccount):
    
    def __init__(self, amount=0) -> None:
        self._amount = amount

    @property
    def amount(self) -> float:
        return self._amount  
    @amount.setter
    def amount(self, value: float):
        self._amount = value