# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

import json
from .DataArcher import DataArcher
from Interfaces.IArcher import IArcher



class Archer(DataArcher, IArcher):
    """ Archer, which can be hit and shoot arrows
    Arguments:
        DataArcher -- sub class containing all member variables
        IArcher -- interface for all archers 
    """
    def __init__(self, myid: int, hitpoints: int, arrows: int):
        super().__init__(myid, hitpoints, arrows)
        # _id = id
        # _hitpoints = hitpoints
        # _arrows = arrows
            
    def __str__(self):
        return f"Archer ID: {str(self._myid)}, hitpoints: {str(self._hitpoints)}, arrows: {str(self._arrows)}"
    
    def shoot(self):
        """ Name: shoot
        Description: shoots an arrow and decrements the number of arrows
        Raises:
            ValueError: if number of arrows is 0 
        """
        try:
            if self._arrows >= 1:
                self._arrows -= 1
            else:
                raise ValueError
        except RuntimeError as e: 
            print(e.__str__())
    
        
    def increase_arrows(self, new_arrows:int):
        """ Name: increase_arrows
        Description: increases the number of arrows of an instance
        Arguments:
            new_arrows -- number of new arrows
        """
        self._arrows += new_arrows
        
    def toJson(self):
        """ exports the instance dictionary to a json format
        Returns:
            json dump of instance dictionary in format keyword = value
        """
        return json.dumps(self, default=lambda o: o.__dict__)
        