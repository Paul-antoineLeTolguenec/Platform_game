# -*- coding: utf-8 -*-
"""
Je teste le bon fonctionnement de la classe Robot. Je vérifie d'abord l'initialisation des variables d'instances,
puis je vérifie si un robot n'est pas une bombe. Je vérifie aussi la méthode poursuivre.

@author: melan
"""

import unittest

from Monde import Monde
from Mur import Mur
from Element import Element
from Personnage import Personnage

monde=Monde(50,40)

from Ennemi import Bombe,Robot

class TestRobot(unittest.TestCase):
        
    def testRobot(self):
        mur=Mur(monde,25, 20, 6, 2)
        robot = Robot(monde, mur)
        self.assertIsInstance(robot, Element)
    
    def testEnnemis(self):  #je teste si un robot n'est pas une bombe
        mur = Mur(monde, 25, 20, 6,2)
        bombe = Bombe(monde, 10,11)
        robot = Robot(monde, mur)
        self.assertIsNot(bombe, robot)
        
    def testPoursuivre(self):  #avec un exemple de vitesse, on vérifie si le robot poursuit correctement
        mur = Mur(monde, 25, 20, 6,2)
        bombe = Bombe(monde, 10,11)
        robot = Robot(monde, mur)
        perso= Personnage(monde, 5,8,1,1)
        
        side1 = 'droite'
        Robot.poursuivre(robot,side1)
        self.assertEqual(robot._vitesse, (robot.vitesse_poursuite,0))
        
        side2 = 'gauche'
        Robot.poursuivre(robot,side2)
        #print(robot._vitesse)
        self.assertEqual(robot._vitesse, (-robot.vitesse_poursuite,0))
    
if __name__ == '__main__':
    unittest . main ()
    
