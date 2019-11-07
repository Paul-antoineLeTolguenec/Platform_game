# -*- coding: utf-8 -*-
"""
dans cette classe je vais créer la simulation.
Cette partie du code va me permettre de gérer le temps. Et donc de mettre à jour le jeu en permanence toute les 0.04 seconde.
je fais hériter la classe par thread de façon à pouvoir gérer cet objet en même temps qu'un autre.
Une variable d'instance de cet objet sera la fenêtre qui est l'autre objet que je vais gérer en même temps. Ceci va permettre la communication entre les 2 objets.


@author: letol
"""


import sys
from threading import Thread
import time
from Monde import Monde
from Personnage import Personnage
#from Fenetre import Fenetre
import sys

class Simulation(Thread):

    def __init__(self, personnage,fenetre):
        Thread.__init__(self)
        self.personnage = personnage
        self.fenetre=fenetre
        self.nb_exec=0

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        tfin=time.time()
        
        tf=time.time()
        if self.nb_exec==0:
            while self.fenetre.etat_jeu=="off":
                pass
            while tf-tfin<=self.personnage.temps_vie:
                tf=time.time()
                time.sleep(0.03) #j'ai décidé de le faire toute les 0.03 secondes pour que cela soit plus fluide. effet accéléré.
                self.fenetre.centralwidget.update()
                self.personnage.update()
                self.personnage.monde.update()
                if self.personnage.etat_perso=="mort"or self.personnage.etat_jeu=="gagné":
                    self.fenetre.centralwidget.update()
                    break
                
        self.nb_exec=self.nb_exec+1
                
               
            
            
if __name__=="__main__":
    pass