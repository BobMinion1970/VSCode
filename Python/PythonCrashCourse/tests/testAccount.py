import unittest
from src.interfaces.IAccount import IAccount
from src.classes.Account import Account

class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account: IAccount = None
        self.account = Account(1000.00)
        print("After setup: " +str(self.account.credit))
        
    def test_GetterCredit(self): 
        self.assertEqual(self.account.credit, 1000.00)
        
    def test_SetterCredit(self):
        self.account.credit += 500.00
        self.assertEqual(self.account.credit, 1500.00)
        print(f"Credit after deposit: {self.account.credit}")