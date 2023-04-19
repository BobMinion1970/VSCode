def main():
    try:
        TestArrayHandling()
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
        raise Exception("Tom does not exist")
    
    _length = len(_namelist)
    _index = 0

    while _index < _length:
        print(_namelist[_index])
        _index = _index + 1

main()
