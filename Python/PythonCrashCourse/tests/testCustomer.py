import unittest
import datetime
from src.interfaces.ICustomer import ICustomer
from src.interfaces.IAccount import IAccount
from src.classes.Customer import Customer
from src.classes.Account import Account
#from .context import ICustomer, Customer
class CustomerTest(unittest.TestCase):   
    def setUp(self):
        self.account: IAccount = None
        self.customer: ICustomer = None
        self.account = Account(1000.00)
        self.customer = Customer(1000, "Bob", "Minion")
        self.customer.account = self.account
        print("################################ Module CustomerTest ####################################")
        print("Started at: " + str(datetime.datetime.now()))
        print("After setup: " +str(self.customer.account.credit))
    
    def test_AddMoneyToAccount(self):
        print("Test case name: test_AddMoneyToAccount") 
        self.customer.AddMoneyToAccount(100.00)
        self.assertEqual(self.customer.account.credit, 1100.00)
    
    def test_AddNegativeMoneyToAccount(self):  
        print("Test case name: test_AddNegativeMoneyToAccount")                 
        with self.assertRaises(ArithmeticError): 
            self.customer.AddMoneyToAccount(-100.00)
            
    def test_RemoveMoneyFromAccountWitEnoughCredit(self):
        print("Test case name: test_RemoveMoneyFromAccountWitEnoughCredit")               
        print(f"Current credit: {self.customer.account.credit}")
        self.customer.RemoveMoneyFromAccount(900)
        print(f"Current credit after removal: {self.customer.account.credit}")
        self.assertGreaterEqual(self.customer.account.credit, 0.00)
    
    def test_RemoveMoneyFromAccountWithNotEnoughCredit(self):
        print("Test case name: test_RemoveMoneyFromAccountWithNotEnoughCredit")
        print(f"\nCurrent credit: {self.customer.account.credit}")
        print(f"Payment: 1100")
        with self.assertRaises(ArithmeticError):
            self.customer.RemoveMoneyFromAccount(1100.00)
            print(f"Current credit after removal: {self.customer.account.credit}")
    
    def test_GetterFirstName(self):
        print("Test case name: test_GetterFirstName") 
        self.assertEqual(self.customer.firstname, "Bob")
    
    def test_SetterFirstName(self): 
        print("Test case name: test_SetterFirstName")
        print(f"\nCurrent first name: {self.customer.firstname}")
        self.customer.firstname = "Kevin"
        self.assertEqual(self.customer.firstname, "Kevin")
        print(f"Changed first name: {self.customer.firstname}")
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(exit=False)
            