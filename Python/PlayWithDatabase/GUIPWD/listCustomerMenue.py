import os
import logging
import DB

def listcustomermenue(_db: DB.DBSingleton) -> None:
    os.system("cls")  
    print("##################################### List Customers - Sub Menue #####################################")    
    row = _db.execute("SELECT * FROM Customer")
  
    print(row)
    c = input("Type enter to return to main menue")