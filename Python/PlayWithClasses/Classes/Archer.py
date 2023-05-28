# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from IArcher import IArcher

class Archer(IArcher):

    def __init__(self, id: int, hitpoints: int, arrows: int):
        self._id = id
        self._hitpoints = hitpoints
        self._arrows = arrows
    
    def __str__(self):
        return f"Archer ID: {str(self._id)}, hitpoints: {str(self._hitpoints)}, arrows: {self._arrows}"
    
    def shoot(self):
        if self._arrows >= 1:
            self._arrows -= 1
        else:
            raise ValueError
        
    def increase_arrows(self, new_arrows:int):
        self._arrows += new_arrows
        