from src.interfaces.IAccount import IAccount

class Account(IAccount):
    
    def __init__(self, amount=0) -> None:
        self._credit = amount

    @property
    def credit(self) -> float:
        return self._credit  
    @amount.setter
    def credit(self, value: float) -> None:
        self._credit = value