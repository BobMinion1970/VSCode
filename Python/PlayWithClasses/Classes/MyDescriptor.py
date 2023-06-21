# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
#import pdb
from typing import Any


class MyDescriptor():
    
    def __init__(self, value) -> None:
        self._value = value
    
    def __getattr__(self, name: str) -> Any:
        return self.__dic__[name]
    
    def __setattr__(self, name: str, value: Any) -> None:
       self.__dict__[name] = value