from src.interfaces.ICustomer import IOrder


class Order(IOrder):
    
    def __init__(self, customerID: str) -> None:
        self._customerID = customerID
        self._orderitemlist = list()

    @property
    def orderitemlist(self) -> list:
        return self._orderitemlist
    
    def addorderitem(self, orderitem) -> None:
        self._orderitemlist.add(orderitem)