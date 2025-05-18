import unittest
import os 
from pathlib import Path
os.chdir("..")

from src.business import Account
from src.business import Customer
from src.database import Accounts

class Test_Account(unittest.TestCase):
    def setUp(self):
        self._account =  Account.Account(1,"1000",110.5)
        return super().setUp()
    
    def test_add_to_balance(self):
        print("New account: id: {}, balance: {}, customerid: {}".format(self._account.account_id, self._account.balance, self._account.customer_id) )
        self._account.add_to_balance(10.2)
        self.assertEqual(self._account.balance, 120.7)
        print("New account after adding a balance of 10.2: id: {}, balance: {}, customerid: {}".format(self._account.account_id, self._account.balance, self._account.customer_id) )
          
    def test_debit_from_account(self):
        self._account.balance -= 100
        self.assertEqual(self._account.balance, 10.5)

    def test_adding_balance_to_locked_account(self):
        print("Account before adding a balance of 10.2: id: {}, balance: {}, customerid: {}".format(self._account.account_id, self._account.balance, self._account.customer_id) )
        self._account.lock_account(True)
        try: 
            self._account.add_to_balance(10.2)
        except AttributeError:
            self.assertTrue("No balance added")
            print("Account after adding a balance of 10.2: id: {}, balance: {}, customerid: {}".format(self._account.account_id, self._account.balance, self._account.customer_id) )

    def test_debiting_balance_to_locked_account(self):
        print("Account before debiting a balance of 10.2: id: {}, balance: {}, customerid: {}".format(self._account.account_id, self._account.balance, self._account.customer_id) )
        self._account.lock_account(True)
        try: 
            self._account.add_to_balance(10.2)
        except AttributeError:
            self.assertTrue("No balance added")
            print("Account after debiting a balance of 10.2: id: {}, balance: {}, customerid: {}".format(self._account.account_id, self._account.balance, self._account.customer_id) )  
        
if __name__ == '__main__':
    os.chdir("..")
    unittest.main()
    