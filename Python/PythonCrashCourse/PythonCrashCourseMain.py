# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from src.interfaces.IAccount import IAccount
from src.interfaces.ICustomer import ICustomer
from src.classes.Customer import Customer
from src.classes.Account import Account


def main() -> None:
    account1 : IAccount = None
    account2 : IAccount = None
    customer1: ICustomer = None
    customer2: ICustomer = None
    
    account1 = Account(1000.11)
    customer1 = Customer("Bob", "Minion", account1)
    print("Name by method GetFullName")
    print(customer1.getFullName())
    print("Amount customer1: " + str(customer1.account.amount))
    
    account2 = Account(2000.22)
    customer2 = Customer();
    customer2.firstname = "Kevin"
    customer2.lastname = "Minion"
    customer2.account = account2
    print("Name by properties")
    print(customer2.firstname + ", " + customer2.lastname)
    print("Amount customer2: " + str(customer2.account.amount))
   
    
main()

