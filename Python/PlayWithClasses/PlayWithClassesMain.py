# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error

# import pdb
# import os
# import sys
# pdb.set_trace()
# _rootpath = os.getcwd()
# _mainpath = _rootpath + "\\Python\\PlayWithClasses"
# os.chdir(_mainpath)
# # sys.path.append(_path)

from Interfaces import ICompany
from Interfaces import IBow
from Classes import Archer
from Classes import Company
from Classes import ElveBow
from Classes import ArcherWithDescriptor

######################################## Functions ####################################
def main():
   
    try: 
        print("################################### WOA ###################################")
        print("######################## World of Archers started #########################")
        # pdb.set_trace()
        _archer1 = Archer.Archer(1001, 10, 100)
        print(_archer1)
        print("Archer1 shoots one arrow")
        _archer1.shoot()
        print(_archer1)
        _archer2 = Archer.Archer(2002,20, 200)
        print(_archer2)
        print("Archer2 shoots one arrow")
        _archer2.shoot()
        _archer2._magic = "Full"    # dynamic attribute, which exists only in this instance
        print(_archer2)
        print("New attribute <magic> in instance archer2: " + _archer2._magic)
        try:
            print(_archer1.magic)
        except AttributeError: 
            print("Attribute Error caught: No attribute <magic> in instance archer1")
        
        _company = Company.Company()
        # pdb.set_trace()
        _company.add(_archer1)
        _company.add(_archer2)
        #print(_company._archers)
        print("Company: ")
        print(_company.__str__())
        _archer1.increase_arrows(150)
        print("Added 150 arrows to Archer1")
        print(_archer1)
        print("Company:")
        print(_company.__str__())
        try:
            _elveBow1 = ElveBow.ElveBow(strength = "Strong", material = "Oak")
            print(_elveBow1)
            _elveBow1.strength = "Medium"
        except AttributeError as e:
            print("Setter missing: " + e.__str__() )
        
        # force a type error from class Company
        print("Changed bow: " + _elveBow1.__str__())
        try:
            _company.add(_elveBow1)
        except TypeError as _e: 
            print("My wished error is: TypeError" + _e.__str__())
        
        # print object dictionary as json structure 
        print("Archer 1: " + _archer1.toJson())
        print("Archer 2: " + _archer2.toJson())  # dynamic attribute magic will be printed
        _archer3 = ArcherWithDescriptor(myid=3003, hitpoint = 10, arrows=100)
        print(f"Archer with Dewcriptor: {_archer3}")
    except ValueError as e:
        print(e.__str__())
    

########################################### Main ######################################
main()
