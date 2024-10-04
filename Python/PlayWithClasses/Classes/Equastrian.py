class Equastrian():
    """ class for equastrian 
    Attribute: weapon
    """
    @property
    def weapon (self) -> str:
        return self._weapon
    
    @weapon.setter
    def weapon(self, value: str) -> None:
        if type(value) == str:
            self._weapon = value
        else:
            raise TypeError