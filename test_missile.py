# -*- coding: utf-8 -*-
"""
Je teste la classe Missile. D'abord je m'assure que les variables d'instances sont bien initialisées.
Je vérifie que la méthode toucher() renvoie bien False ou True dans les où le personnage est touché ou pas. 
Je vérifie ensuite les méthodes poursuivre() et update() en comparant les vitesses et les coordonnées du missile.

@author: melan
"""
import unittest
import numpy as np

from Monde import Monde
from Ennemi import Bombe, Robot, Missile
from Personnage import Personnage

monde = Monde(50,40)

class TestMissile(unittest.TestCase):
    
    def testMissile(self):
        """vérification de la bonne instanciation de missile"""
        missile = Missile(monde)
        self.assertEqual(missile._coords, (49,39))
        #self.assertEqual(missile.Y, 39)
        self.assertEqual(missile.largeur, 1)
        self.assertEqual(missile.hauteur, 1)
        
    
        
    def testPoursuivre(self):  #vérifie si le missile poursuit bien le personnage qui est à un certain angle. 
        missile = Missile(monde)
        print(missile._vitesse)
        Missile.poursuivre(missile, 45)  #Ici je choisi de tester avec 45 degrés
        print(missile._vitesse)
        self.assertEqual(missile._vitesse , (6*np.cos(45),6*np.sin(45)))
        
    
        
if __name__=="__main__":
    unittest.main()

    