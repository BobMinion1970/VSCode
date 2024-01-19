import unittest
from src.interfaces.ICustomer import ICustomer
from src.interfaces.IAccount import IAccount
from src.classes.Customer import Customer
from src.classes.Account import Account

class CustomerTest(unittest.TestCase):     
    
    def setUp(self):
        self.account: IAccount = None
        self.customer: ICustomer = None
        self.account = Account(1000.00)
        self.customer = Customer("Bob", "Minion", self.account)
    
    def test_AddMoneyToAccount(self): 
        self.customer.AddMoneyToAccount(100.00)
        self.assertEqual(self.customer.account.amount, 1100.00)
    
    def test_RemoveMoneyFromAccountWitEnoughCredit(self):
        try:
            print(f"Current amount: {self.customer.account.amount}")
            self.customer.RemoveMoneyFromAccount(900)
            print(f"Current amount after removal: {self.customer.account.amount}")
            self.assertGreaterEqual(self.customer.account.amount, 0.00)
        except ArithmeticError:
            pass
    
    def test_RemoveMoneyFromAccountWithNotEnoughCredit(self):
        try:
            print(f"\nCurrent credit: {self.customer.account.amount}")
            print(f"Payment: 1100")
            self.customer.RemoveMoneyFromAccount(1100.00)
            self.assertEqual(self.customer.account.amount, 1000.00)
        except ArithmeticError:
            print(f"Current credit after removal: {self.customer.account.amount}")
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()        