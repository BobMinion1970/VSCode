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

from Classes import Archer
from Interfaces import ICompany
from Classes import Company

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
    except ValueError as e:
        print(e.__str__())

########################################### Main ######################################
main()
