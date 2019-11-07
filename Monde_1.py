# -*- coding: utf-8 -*-
"""
Dans ce fichier je vais lancer le main 
c'est ici que je réalise toutes les instanciations.
Phase 1: je construit le monde 
phase 2: je remplis le monde de tout les éléments 
phase 3: je crée le personnage
phase 4: je crée la fenêtre et la simulation 
phase 5: je lance les thread ( en mettant bien bien app.exec entre les 2 lancement sinon il ne s'execute qu'à la fin des 2 threads)
@author: letol
"""


from Simulation import Simulation
import time
from Monde import Monde
from Personnage import Personnage
from threading import Thread
import sys
from Personnage import Personnage
from PyQt5.QtCore import Qt
#from PyQt5.QtCore import QString
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QKeyEvent, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from Fenetre import Fenetre
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv) 
    
# création du monde 
monde=Monde(100,90) 

#remplissage du monde avec tout les éléments
monde.creation_Portail(49,80,50,1)
monde.creation_mur(0,0,100,1,"mur")
monde.creation_mur(20,10,60,10,"mur")
monde.creation_mur(20,30,60,10,"mur")
monde.creation_mur(20,50,60,10,"mur")
monde.creation_mur(20,70,10,1,"Plateform")

monde.creation_Robot(monde.murs[0]) 
monde.creation_Robot(monde.murs[1]) 
monde.creation_Robot(monde.murs[2]) 
monde.creation_Robot(monde.murs[3])   

monde.creation_Bombe(80,20)
monde.creation_Bombe(81,20)
monde.creation_Bombe(82,21)
monde.creation_Bombe(83,21)
monde.creation_Bombe(84,22)
monde.creation_Bombe(85,22)
monde.creation_Bombe(86,23)
monde.creation_Bombe(87,23)
monde.creation_Bombe(88,24)
monde.creation_Bombe(89,24)
monde.creation_Bombe(90,25)
monde.creation_Bombe(91,25)
monde.creation_Bombe(92,26)
monde.creation_Bombe(93,26)
monde.creation_Bombe(94,27)
monde.creation_Bombe(95,27)
monde.creation_Bombe(96,28)
monde.creation_Bombe(97,28)
monde.creation_Bombe(98,28)
monde.creation_Bombe(99,28)

monde.creation_Bombe(19,40)
monde.creation_Bombe(18,40)
monde.creation_Bombe(17,41)
monde.creation_Bombe(16,41)
monde.creation_Bombe(15,42)
monde.creation_Bombe(14,42)
monde.creation_Bombe(13,43)
monde.creation_Bombe(12,43)
monde.creation_Bombe(11,44)
monde.creation_Bombe(10,44)
monde.creation_Bombe(9,45)
monde.creation_Bombe(8,45)
monde.creation_Bombe(7,46)
monde.creation_Bombe(6,46)
monde.creation_Bombe(5,47)
monde.creation_Bombe(4,47)
monde.creation_Bombe(3,48)
monde.creation_Bombe(2,48)
monde.creation_Bombe(1,48)
monde.creation_Bombe(0,48)

monde.creation_Bombe(80,59)
monde.creation_Bombe(81,59)
monde.creation_Bombe(82,59)
monde.creation_Bombe(83,59)
monde.creation_Bombe(84,59)
monde.creation_Bombe(85,59)
monde.creation_Bombe(86,59)
monde.creation_Bombe(87,59)
monde.creation_Bombe(88,59)
monde.creation_Bombe(89,59)
monde.creation_Bombe(90,59)
monde.creation_Bombe(91,59)
monde.creation_Bombe(92,59)
monde.creation_Bombe(93,59)
monde.creation_Bombe(94,59)
monde.creation_Bombe(95,59)
monde.creation_Bombe(96,59)
monde.creation_Bombe(97,59)
monde.creation_Bombe(98,59)
monde.creation_Bombe(99,59)

#instanciation de personnage
perso=Personnage(monde,50,60,2,2)
#j'instancie mes objets qui permettent l'IHM
fen = Fenetre(perso)
Sim=Simulation(perso,fen)
#Lancement des threads
Sim.start()

fen.start()



fen.show()

app.exec_()


Sim.run()

