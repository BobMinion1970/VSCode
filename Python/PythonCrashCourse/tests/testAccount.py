import unittest
import datetime
#from .context import IAccount, Account
from src.interfaces.IAccount import IAccount
from src.classes.Account import Account
class AccountTest(unittest.TestCase):
    
    def setUp(self):
        self.account: IAccount = None
        self.account = Account(1010.00)
        print("################################ Module AccountTest ####################################")
        print("Started at: " + str(datetime.datetime.now()))
        print("After setup: " +str(self.account.credit))
        
    def test_GetterCredit(self): 
        print("Test case name: test_GetterCredit") 
        self.assertEqual(self.account.credit, 1010.00)
        
    def test_SetterCredit(self):
        print("Test case name: test_SetterCredit") 
        self.account.credit += 500.00
        self.assertEqual(self.account.credit, 1510.00)
        print(f"Credit after deposit of 500 bucks: {self.account.credit}")
        
if __name__ == '__main__':
    unittest.main(exit=False)
            