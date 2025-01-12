import os
import logging
import DB


def createcustomermenue(_db: DB.DBSingleton) -> None:
    _menueselection : str = ""
    while _menueselection != "x":
        os.system("cls")
        print("################1##################### Create Customer - Sub Menue #####################################")    
        _firstname = input("First name: ")      
        _lastname = input("Last name: " )
        _birthday = input("Birthday: ")
        _menueselection = input("Create new customer y/n: ")
        
        if _menueselection == "y": 
            sqlstring = f"INSERT INTO Customer(FirstName, LastName, BirthDay) VALUES ('{_firstname}', '{_lastname}',' {_birthday}')"
            _db.execute(sqlstring)
            _db._con.commit()
            _menueselection = input("Type 'x' to return to main menue")