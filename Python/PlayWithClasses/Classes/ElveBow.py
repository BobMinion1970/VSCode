# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from Interfaces.IBow import IBow

class ElveBow(IBow):
    
    @property 
    def strength(self) -> str:
        return self._strength
    
    @strength.setter
    def strength(self, value: str) -> None:
        if type(value) == str:
            self._strength = value
        else:
            raise TypeError
    
    @property 
    def material(self) -> str:
        return self._material
    
    def __init__(self, strength, material):
        self._strength = strength
        self._material = material
    
    def __str__(self):
        return f'Strength: {self._strength}; Material: {self._material}' 