import math
import numpy as np

d = {10001 : "Bob", 10002: "Kevin"}

def testfunc():
    d[10001] = "Gru"

def testMoreReturnValues(x):
    return x+10, x+20, x +30

def main():
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

main()