# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error

import sys
import os

path = os.getcwd()
sys.path.insert(0, path)
sys.path.append(path + "\\Classes")
sys.path.append(path + "\\Interfaces")

from Archer import Archer
from ICompany import ICompany
from Company import Company
# import pdb
######################################## Functions ####################################
def main():
    try: 
        print("################################### WOA ###################################")
        print("######################## World of Archers started #########################")
        # pdb.set_trace()
        _archer1 = Archer(1001, 10, 100)
        print(_archer1)
        print("Archer1 shoots one arrow")
        _archer1.shoot()
        print(_archer1)
        _archer2 = Archer(2002,20, 200)
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

        _company: ICompany
        _company = Company()
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
