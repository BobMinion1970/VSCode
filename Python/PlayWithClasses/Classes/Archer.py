# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

from .DataArcher import DataArcher
from Interfaces.IArcher import IArcher

# class ArrowType(StrEnum):
#     L = "Long bow"
#     S = "Short bow"

class Archer(DataArcher, IArcher):
    def __init__(self, myid: int, hitpoints: int, arrows: int):
        super().__init__(myid, hitpoints, arrows)
        # _id = id
        # _hitpoints = hitpoints
        # _arrows = arrows
            
    def __str__(self):
        return f"Archer ID: {str(self._myid)}, hitpoints: {str(self._hitpoints)}, arrows: {str(self._arrows)}"
    
    def shoot(self):
        try:
            if self._arrows >= 1:
                self._arrows -= 1
            else:
                raise ValueError
        except RuntimeError as e: 
            print(e.__str__())
        
    def increase_arrows(self, new_arrows:int):
        self._arrows += new_arrows
        