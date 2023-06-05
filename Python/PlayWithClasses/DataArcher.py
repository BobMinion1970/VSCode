# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
from dataclasses import dataclass

@dataclass()
class DataArcher():
    _id: str
    _hitpoints: int = 0
    _arrows: int = 0
    