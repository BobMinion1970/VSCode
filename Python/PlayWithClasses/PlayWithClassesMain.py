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
######################################## Functions ####################################
def main():
    
    print("################################### WOA ###################################")
    print("World of Archers started")
    archer1 = Archer(1001, 10, 100)
    archer1.shoot()
    print(archer1)
    archer2 = Archer(2002,20, 200)
    archer2.shoot()
    print(archer2)
########################################### Main ######################################
main()
