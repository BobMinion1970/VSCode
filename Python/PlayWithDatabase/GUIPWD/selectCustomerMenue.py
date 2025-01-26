import os
import DB
import Customer
import sqlite3

def selectcustomermenue(_db: DB.DBSingleton) -> None:   
   
    os.system("cls") 
    
    _menueselection : str = ""
    _customerid : str = ""
    _customer : Customer.Customer
    while _menueselection != "x":
        os.system("cls")
        print("##################################### Select Customer - Sub Menue #####################################")  
        _customerid = input("CustomerID: ") 

        row = _db.execute("SELECT * FROM Customer WHERE CustomerID = " + _customerid)    
        print(row)
        _customer = Customer.Customer(row[0][0], row[0][1], row[0][2], row[0][3])
        print("Customer id: " + str(_customer._id))
        print("Customer first name: " + str(_customer._firstname))
        print("Customer last name: " + str(_customer._lastname))
        print("Customer birthday: " + str(_customer._birthday))
        print("Customer age: " + _customer.age())
        

        _menueselection = input("Type 'x' to return to main menue")
