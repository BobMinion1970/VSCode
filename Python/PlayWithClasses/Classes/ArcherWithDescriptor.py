# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
#import pdb
from .MyDescriptor import MyDescriptor

class ArcherWithDescriptor():
          
    def __init__(self, _myid: int, _hitpoints: int, _arrows:int) -> None:
        self.hitpoints = MyDescriptor("hitpoints")
        self.arrows = MyDescriptor("arrows")
        self.myid = MyDescriptor("myid")
        self.myid = _myid
        self.hitpoints =_hitpoints
        self.arrows = _arrows
        
    def __str__(self) -> str:
        return f"Archer ID: {str(self.myid)}, hitpoints: {str(self.hitpoints)}, arrows: {str(self.arrows)}"