import unittest
import datetime

from Interfaces.IArcher import IArcher
from Classes.Archer import Archer


class ArcherTest(unittest.TestCase):
    def setUp(self):
        self.archer: IArcher = None
        self.archer = Archer(1111, 0, 200)
        print("Started at: " + str(datetime.datetime.now()))
        print("Arrows after setup: " +str(self.archer._arrows))
        
    def test_GetterArrows(self): 
        print("Test case name: test_Arrows") 
        self.assertEqual(self.archer._arrows, 200)
        
    def test_SetterArrows(self):
        print("Test case name: test_SetterArrows") 
        self.archer._arrows += 10.00
        print(f"Arrows after deposit of 10 arrows: {self.archer._arrows}")
        self.assertEqual(self.archer._arrows, 210.00)
       
    def test_Shoot_ValidArrows(self):
        self.archer._arrows = 3
        print("Test case name: Test_Shoot_ValidArrows") 
        print(f"Arrows before shoot: {self.archer._arrows}")  
        self.archer.shoot()
        self.archer.shoot()
        self.assertEqual(self.archer._arrows, 1)
        
    def test_Shoot_InvalidArrows(self):
        self.archer._arrows = 1
        print("Test case name: Test_Shoot_InvalidArrows") 
        print(f"Arrows before shoot: {self.archer._arrows}")  
        self.archer.shoot()
        print(f"Arrows after first shot: {self.archer._arrows}")  
        try:
           self.archer.shoot()
        except ValueError as e:
           self.assertTrue("ValueError catched")
           print(f"Value Error was raised, because archer has too few arrows!")

if __name__ == '__main__':
    unittest.main(exit=False)
