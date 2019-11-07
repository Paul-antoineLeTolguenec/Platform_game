# -*- coding: utf-8 -*-
"""
Je teste la classe Mur

@author: melan
"""
import unittest

from Monde import Monde
from Mur import Mur, Plateforme

class TestMur(unittest.TestCase):
    
    def testMur(self):
        mur = Mur(monde, 25, 20, 6, 2)
        plateforme = Plateforme(monde, 14, 10, 5,1)
        self.assertIsInstance(mur, Element)  #vérifie si un mur et une plateforme sont bien des élements
        self.assertIsInstance(plateforme, Element)
    
        self.assertIsNot(mur, plateforme)  # vérifie si un mur n'est pas une plateforme

if __name__ == '__main__':
    unittest.main()