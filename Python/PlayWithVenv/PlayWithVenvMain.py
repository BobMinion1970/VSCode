from src.business import Account
from src.business import Customer
from src.database import Accounts

def main() -> None:
    accounts = Accounts.Accounts()

    customer1: Customer.Customer = Customer.Customer("S100", "Minion", "Bob", 1000)
    account1 = Account.Account(1000, "S100", 312.50)
    
    print("Customer 1:")
    print(customer1.__dict__)
    print("Account 1:")
    print (account1.__dict__)
    accounts.add_account(account1)
    account2 = Account.Account(1001, "S100", 412.00)
    accounts.add_account(account2)

    print("Account list: ")
    for account in accounts.accounts:
        print (account.__dict__)

main()