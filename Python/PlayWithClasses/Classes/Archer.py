class Archer:

    def __init__(self, id, hitpoints, arrows):
        self._id = id
        self._hitpoints = hitpoints
        self._arrows = arrows
    
    def __str__(self):
        return f"Archer ID: {self._id}, hitpoints: {self._hitpoints}, arrwos: {self._arrows}"
    