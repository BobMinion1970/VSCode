import os
import logging
import DB

def selectcustomermenue(_db: DB.DBSingleton) -> None:   
   
    os.system("cls") 
    #pdb.set_trace()
    _menueselection : str = ""
    _customerid : str = ""
    while _menueselection != "x":
        os.system("cls")
        print("##################################### Select Customer - Sub Menue #####################################")  
        _customerid = input("CustomerID: ") 
        row = _db.execute("SELECT * FROM Customer WHERE CustomerID = " + _customerid)    
        print(row)
        _menueselection = input("Type 'x' to return to main menue")
