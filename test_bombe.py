# -*- coding: utf-8 -*-
"""
Je teste la classe Bombe

@author: melan
"""
import unittest

from Monde import Monde
from Ennemi import Bombe,Robot

monde=Monde(50,40)

class TestBombe(unittest.TestCase):
    def testBombe(self):
        bombe = Bombe(monde, 10,11)
        self.assertEqual(bombe.coords, (10,11))
        self.assertEqual((bombe.hauteur,bombe.largeur),(1,1)) #vérifie si la bombe a la bonne dimension 1x1
        #self.assertIsInstance(bombe, Element)
        
if __name__ == '__main__':
    unittest . main ()
