# -*- coding: utf-8 -*-
"""
Ici je vérifie la classe Plateforme avec ses variables. 
Je teste aussi si un mur et une plateforme aux mêmes coordonnées ne sont confondus.

@author: melan
"""

import unittest

from Monde import Monde
from Element import Element
from Mur import Plateforme, Mur

monde = Monde(50,40)

class TestPlateforme(unittest.TestCase):
    def testInit(self):
        plateforme = Plateforme(monde, 15, 22, 10, 3)
        self.assertEqual(plateforme.coords,(2,4))
        self.assertEqual(plateforme.hauteur, 4)
        self.assertEqual(plateforme.largeur, 5)
        self.assertEqual(plateforme.vitesse_mouv,5)
        self.assertEqual(plateforme._vitesse, (5,0))
        
    def testMurs(self):
        mur = Mur(monde, 15, 22, 10, 3)
        plateforme = Plateforme(monde, 15, 22, 10, 3)
        #je vérifie que deux objets de Mur au même endroit ont les mêmes coordonnées mais ne sont pas confondues 
        self.assertEqual(mur, plateforme)
        self.assertIsNot(mur, plateforme)