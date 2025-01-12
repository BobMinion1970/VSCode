import os
import logging
#from GUIPWD import selectCustomerMenue
from Database import DB
from GUIPWD import selectCustomerMenue, createCustomerMenue, listCustomerMenue

def mainmenue(db: DB.DBSingleton) -> None:
    _menueselection : str = ""
   
        
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
            createCustomerMenue.createcustomermenue(db)
        if _menueselection == "2":
            selectCustomerMenue.selectcustomermenue(db)
        if _menueselection == "3":
            listCustomerMenue.listcustomermenue(db)


