from abc import ABC, abstractmethod

class IOrder(ABC):
      
    @property
    @abstractmethod
    def orderitemlist(self) -> list:
       pass