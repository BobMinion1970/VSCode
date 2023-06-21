# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
#import pdb
import .MyDescriptor

class ArcherWithDescriptor():
   
    def __init__(self, myid: int, hitpoints: int, arrows:int) -> None:
        self._myid = MyDescriptor(myid)
        self._hitpoints = MyDescriptor(hitpoints)
        self._arrows = MyDescriptor(arrows)
        
    def __str__(self):
        return f"Archer ID: {str(self._myid)}, hitpoints: {str(self._hitpoints)}, arrows: {str(self._arrows)}"