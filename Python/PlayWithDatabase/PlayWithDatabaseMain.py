# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error

#import pdb
import os
import sqlite3
from Database import DB
# from .Business import Customer1

# import sys
# pdb.set_trace()
# _rootpath = os.getcwd()
# _mainpath = _rootpath + "\\Python\\PlayWithClasses"
# os.chdir(_mainpath)
# # sys.path.append(_path)
db = None 
cursor = None
    
def mainmenue() -> None:
    _menueselection : str = ""
    global db
    global cursor
    try:
        db = sqlite3.connect("E:\Develop\Projects\TAT\VSCode\Python\PlayWithDatabase\PlayWithDatabase.db")
        cursor = db.cursor()
        #dbcustomer = new DBCustomer(db, cursor)
        
    except sqlite3.Error as e:    
        print(e)
        
    while _menueselection != "x":
        os.system("cls")
        print(dir(__builtins__))
        print("##################################### Customer Management System  - Main Menue #####################################")    
        print("1 - Create a new customer")  
        print("2 - Select customer")
        print("3 - List customers")
        print("x - Exit")
        _menueselection = input("Selection: ")
        if _menueselection == "1":
            createcustomermenue()
        if _menueselection == "2":
            selectcustomermenue()
        if _menueselection == "3":
            listcustomermenue()

def createcustomermenue() -> None:
    _menueselection : str = ""
    while _menueselection != "x":
        os.system("cls")
        print("################1##################### Create Customer - Sub Menue #####################################")    
        _firstname = input("First name: ")      
        _lastname = input("Last name: " )
        _birthday = input("Birthday: ")
        _menueselection = input("Create new customer y/n: ")
        
        if _menueselection == "y": 
            cursor.execute("INSERT INTO Customer(FirstName, LastName, BirthDay) VALUES (?, ?, ?)", (_firstname, _lastname, _birthday))
            db.commit()

def selectcustomermenue() -> None:   
    os.system("cls") 
    #pdb.set_trace()
    print("##################################### Select Customer - Sub Menue #####################################")  
    _customerid = input("CustomerID: ") 
    cursor.execute("SELECT * FROM Customer WHERE CustomerID = " + _customerid)
    row = cursor.fetchall()
    print(row)
    c = input("")

def listcustomermenue() -> None:
    os.system("cls")  
    print("##################################### List Customers - Sub Menue #####################################")    
    cursor.execute("SELECT * FROM Customer")
    row = cursor.fetchall()
    print(row)
    c = input("")

def main() -> None:
    mainmenue()
    
main()
