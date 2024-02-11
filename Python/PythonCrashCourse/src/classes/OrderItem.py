# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from src.interfaces.IOrderItem import IOrderItem

class OrderItem(IOrderItem):
    def __init__(self, productname, quantity: int, price: float) -> None:
        self._productname = productname
        self._quantity = _quantity
        self._price = price
    
    def getItem(self) -> str:
        return f"{self._productname}, {self._quantity}, {self._price}"
    
    def getSum(self) -> float:
        return self._quantity * self._price