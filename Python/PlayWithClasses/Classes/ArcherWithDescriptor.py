# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
#import pdb
from .MyDescriptor import MyDescriptor

class ArcherWithDescriptor():
       
    _hitpoints = MyDescriptor()
    _arrows = MyDescriptor()
    _myid = MyDescriptor()
    
    def __init__(self, myid: int, hitpoints: int, arrows:int) -> None:
        _myid = myid
        _hitpoints =hitpoints
        _arrows = arrows
        
    def __str__(self) -> str:
        return f"Archer ID: {str(self._myid._value)}, hitpoints: {str(self._hitpoints._value)}, arrows: {str(self._arrows._value)}"