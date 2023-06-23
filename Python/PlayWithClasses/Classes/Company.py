# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
#import pdb
from Interfaces.IArcher import IArcher 
from Interfaces.ICompany import ICompany

class Company(ICompany):
    maxcount : int = 100
        
    def __init__(self, companyname):
        self._archers = []
        self._companyname = companyname
        self._actualcount = 0
    
    def __str__(self):
        #pdb.set_trace()
        _retval = f"Company name: {self._companyname}\nMax count: {Company.maxcount}\nActual count: {self._actualcount}\nArchers:\n" 
        for a in self._archers:
            _retval += str(a._myid) + ": " + str(a._hitpoints) + ": " + str(a._arrows) + "\n"
        return _retval
         
    def __repr__(self):
        _retval = ""
        for a in self._archers:
            _retval = str(a._myid) + ": " + str(a._hitpoints) + ": " + str(a._arrows) + "\n"
        return _retval
                  
    def add(self, other):
        self.__add__(other)
        
    def __add__(self, other):
        if isinstance(other, IArcher):
            self._archers.append(other)
            self._actualcount += 1
        else:
            raise TypeError
        
    @property 
    def actualcount(self) -> int:
        return self._actualcount
    
    @actualcount.setter
    def strength(self, value: int) -> None:
        if type(value) == int:
            self._actualcount = value
        else:
            raise TypeError
         
        