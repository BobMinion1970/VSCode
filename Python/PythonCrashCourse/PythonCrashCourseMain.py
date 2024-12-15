# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from src.interfaces.IAccount import IAccount
from src.interfaces.ICustomer import ICustomer
from src.classes.Customer import Customer
from src.classes.Account import Account
import argparse
import json
import os
import collections

def main() -> None:
    ############# region for command line arguments ###############
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', dest='infile')
    args = parser.parse_args()
    if args.infile:
        print("Command line argument for input file: " + args.infile)
    
    print("Current folder: " + os.getcwd())
    ############ region where json data comes in ##################
    customers = {}
    with open("Customers.json", mode="r", encoding="utf-8") as input_file:
        try: 
            customers = json.load(input_file)
            print ("Type customers: " + str(type(customers)))
            
            customerlist = customers["Customers"]
            print ("Type customerlist: " + str(type(customerlist)))
           
            searchfirstname = input("Which name should be searched: ")
                           
            #print(customers)
            for index in range(len(customerlist)):
                print("Type of one customer: " + str(type(customerlist[index])))
                if customerlist[index]["firstname"] == searchfirstname:
                    print(customerlist[index])
                
           
        except FileNotFoundError:
            print(f"File not found: {input_file}")
        except Exception:
            print(f"{Exception}")
    
    ############ region for object oriented style #################
    account1 : IAccount = None
    account2 : IAccount = None
    customer1: ICustomer = None
    customer2: ICustomer = None

    account1 = Account(1000.11)
    customer1 = Customer(1000, "Bob", "Minion", account1)
    print("Name by method GetFullName")
    print(customer1.getFullName())
    print("Amount customer1: " + str(customer1.account.credit))
    
    account2 = Account(2000.33)
    customer2 = Customer()
    customer2.firstname = "Kevin"
    customer2.lastname = "Minion"
    customer2.account = account2
    print("Name by properties")
    print(customer2.firstname + ", " + customer2.lastname)
    print("Credit customer2: " + str(customer2.account.credit))
    customer2.AddMoneyToAccount(2.22)
    print(f"Actual credit: {customer2.account.credit}")
    try: 
        customer2.AddMoneyToAccount(-300)
    except ArithmeticError:
        print(f"Credit may not be negative")
    try:
        customer2.RemoveMoneyFromAccount(500)
        print(f"Actual credit: {customer2.account.credit}")
        
        customer2.RemoveMoneyFromAccount(2000)
        print(f"Actual credit: {customer2.account.credit}")
    except ArithmeticError: 
        print(f"Credit is too low: {customer2.account.credit} Please reduce the required withdrawal: 2000")

    
############################################### Main ###########################################
main()
