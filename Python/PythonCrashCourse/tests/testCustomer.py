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
    
    def test_RemoveMoneyFromAccount(self):
        self.customer.RemoveMoneyFromAccount(1000)
        self.assertGreaterEqual(self.customer.account.amount, 0.00)
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()        