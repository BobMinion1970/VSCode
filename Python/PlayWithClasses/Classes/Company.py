# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
#import pdb
from Interfaces.IArcher import IArcher 
from Interfaces.ICompany import ICompany

class Company(ICompany):
        
    def __init__(self):
        self._archers = []
    
    def __str__(self):
        #pdb.set_trace()
        _retval = ""
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
         
        