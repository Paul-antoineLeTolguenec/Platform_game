# -*- coding: utf-8 -*-
"""
Je teste la classe Element. D'abord je vérifie la bonne initialisation puis je teste la méthode update.

@author: melan
"""

import unittest

from Monde import Monde
from Personnage import Personnage


monde=Monde(50,40)

from Element import Element
from Mur import Mur, Plateforme

class TestElement(unittest.TestCase):
    
    def testInit(self):           # vérifie que l'élement est bien initialisé
        element = Element(monde, 2,4,5,4)
        self.assertEqual(element.coords,(2,4))
        self.assertEqual(element.hauteur, 4)
        self.assertEqual(element.largeur, 5)
        self.assertEqual(element._vitesse, (0,0))
        
    def testUpdate(self):        # vérifie que l'élement se déplace correctement
        element = Element(monde, 2,4,5,4)
        dt=0.04 #40 milisec
        (X,Y)=element.coords
        (Xp,Yp)=element._vitesse
        X=dt*Xp+X
        element.coords=(X,Y)
        
        self.assertEqual(element.coords, (X,Y))
        self.assertEqual(element._vitesse, (Xp,Yp))
        
    
if __name__ == '__main__':
    unittest . main ()
