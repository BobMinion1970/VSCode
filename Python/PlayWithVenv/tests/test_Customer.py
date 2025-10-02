import unittest
import os 
from pathlib import Path
os.chdir("..")

from src.business import Account
from src.business import Customer

class Test_Customer(unittest.TestCase):
    def setUp(self):
        self._customer =  Customer.Customer(1,"1000",110.5)
        return super().setUp()

    def test_addAccount_to_empty_accountlist(self):
        print("Accountlist before adding account: {}", self._customer.account_id_list)
        self._customer.addAccount(1000)
        self.assertIn(1000, self._customer.account_id_list)
        print("Accountlist after adding account 1000: {}", self._customer.account_id_list)   
    
    def test_addAccount_to_not_empty_accountlist(self):
        self._customer.addAccount(1000)
        print("Accountlist before adding account: {}", self._customer.account_id_list)
        self._customer.addAccount(1001)
        self.assertIn(1001, self._customer.account_id_list)
        print("Accountlist after adding account 1001: {}", self._customer.account_id_list)   

    def test_removeAccount(self):
        self.fail("This test is not yet implemented.")
