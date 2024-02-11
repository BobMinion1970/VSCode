from abc import ABC, abstractmethod

class IOrderItem():
    @abstractmethod
    getSum(self) -> float:
        pass
    
    @abstractmethod
    getItem(self) -> str:
        pass