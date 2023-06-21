# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
#import pdb

class MyDescriptor():
    def __set__name__(self, owner, name):
        self.name = name
    
    # def __init__(self, value) -> None:
    #     self._value = value
    
    def __get__(self, instance, objtpye=None) -> object:
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value) -> None:
        instance.__dict__[self.name] = value