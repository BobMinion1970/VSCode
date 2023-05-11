from datetime import datetime, timedelta
from array import array

############################################ Classes #####################################
class Person():
    """ Klasse allgemeine Eigenschaften von Personen 
    Attributes: Name, Ort
    """
    def __init__(self, name, ort, geburtsdatum):
        self.Name = name
        self.Ort = ort
        self.Geburtsdatum = geburtsdatum
    
    def printPerson(self):
        """Method printPerson"""
        print(self.Name + ", " + self.Ort + ", " + self.Geburtsdatum)
        
class Customer(Person):
    """ Klasse allgemeine Eigenschaften von Customer 
    Attributes: Account, Balance 
    """
    def __init__(self, _person, _account, _balance):
        super().__init__(_person.Name, _person.Ort, _person.Geburtsdatum)
        self.balance = _balance
        self.account = _account

########################################### Functions ####################################
def main():
    try:
        TestCollections()
        #TestArrayHandling()
    except Exception as e: 
        print(e.__str__())
    finally:
        print("Good bye, have pleasure wherever you are!")
     
def TestArrayHandling():
    print ("Hello PyWorld")
    _name = input("Gib was ein: ") 
    print(_name)
    if _name == "Python":           # : und einrücken der nächsten Zeile!
        print("Checkedin in PyWorld")
        print("********************")
    else:
        print("Failure")

    _namelist = []
    _namelist.append("Kevin")
    _namelist.append("Bob")
    _namelist.append("Stuart")
    try:
        _namelist.remove("Tom")
    except:
        print("Tom does not exist!")
        print("Jerry does not exist!")
        raise Exception("Tom does not exist")
    
    _length = len(_namelist)
    _index = 0

    while _index < _length:
        print(_namelist[_index])
        _index = _index + 1

def TestClasses():
    p2 = Person("Michael", "Büchenbach", "01.01.2001")
    #print(p1.__dict__())
    p2.printPerson()

def TestCustomer():
    _name = input("Name: ")     
    _ort = input("Ort: ") 
    _geb = input("Geburtstag (dd/mm/yyyy): ")
    _person = Person(_name, _ort, _geb)
    print("Person name: " + _person.Name)
    _konto = input("Account: ")
    _balance = float(input("Balance: "))
    _customer = Customer(_person, _konto, _balance)
    print("Customer name: " + _customer.Name)
   #print(_person.__dict__())
   
def TestCollections():
    print("############################# Arrays #####################################")
    _numbers = array('i')
    _numbers.append(5)
    _numbers.append(7)
    print("Array numbers: " + str(_numbers[0]) + ", " + str(_numbers[1]))
  
    print("############################# Lists #####################################")
    _minions = ["Kevin", "Bob", "Stuart", "Dave"]
    print("Before sort: {0}, {1}, {2}, {3}".format(_minions[0], _minions[1], _minions[2], _minions[3]))
    _minions.sort()
    print("After sorted ascending: {0}, {1}, {2}, {3}".format(_minions[0], _minions[1], _minions[2], _minions[3]))
    
    print("########################### Dictionaries ##################################")
    _moreMinions = {}
    _moreMinions['A'] = "Bob"
    _moreMinions['B'] = "Stuart"
    _moreMinions['C'] = "Dave"
    _moreMinions['4'] = "Kevin"
    print(_moreMinions["4"])
    
###################################### Main #####################################
main()
