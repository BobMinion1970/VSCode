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
        

########################################### Functions ####################################
def main():
    try:
        TestClasses()
        #TestArrayHandling()
    except Exception: 
        print("something went wrong")
    finally: 
        print("But we will continue soon!")
     
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
    
###################################### Main #####################################
main()
    #print("%.2d-%.2d-%.4d" % (datum.Tag, datum.Monat, datum.Jahr))  
