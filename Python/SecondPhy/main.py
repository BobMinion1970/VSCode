import math
import os

d = {10001 : "Bob", 10002: "Kevin"}
class punkt(object):
    x = 0
    y = 0

def testfunc():
    d[10001] = "Gru"

def testMoreReturnValues(x):
    return x+10, x+20, x +30

def testChapter1to4():
    a = 5.5
    print(type(a))
    print(math.sqrt(a))
    professor = "Schwandner"
    print(professor[2])
    print(professor[-2])
    print(professor[2:4]) #  hw
    str1 = "ABCDEFGHIJ"
    str2 = "abcdefghij"
    # Schleifenende ist len(str1), da die Schleife
    # einen Durchlauf weniger macht (range-Befehl)
    for index in range(0, len(str1)):
        neustr = str1[index] + str2[-index - 1]
        print("Index: ", index)
        print(neustr)

    #quadrate = [x**2 for x in range(10)]
    #quadrate.pop(5)
    #quadrate.pop(6)
    #print (quadrate)
   
    #_t = tuple()
    #_t = 10, 20, 30
    #print(_t)
    result = testMoreReturnValues(3)  
    print(result)

def testChapter5():
    _filepath = "e:\Develop"
    _files = os.listdir(_filepath)
    for _file in _files:
        if os.path.isfile(os.path.join(_filepath, _file)):
            print(_file)

    _p1 = punkt()
    _p1.x = 5 
    _p1.y = 10
    _p2 = punkt()
    _p2.x = 10
    _p2.y = 20

    print(_p1.x)
    print(_p2.x)        

def main():
    #testChapter1to4()
    testChapter5()

main()
