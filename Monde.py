# -*- coding: utf-8 -*-
"""
Dans ce fichier, je crée la classe world. Cette classe me permettra d'instancier différent monde.
Mon monde aura plusieurs variables d'instances, Mais les variables les plus importantes sont la hauteur et la largeur du monde.
Le monde est un repére ortonormmé avec 0<x<L et 0<y<H

@author: letol
"""
from Mur import Mur,Plateforme
from Ennemi import Bombe,Robot,Missile
from Portail import Portail
class Monde():
    def __init__(self,L,l):
        self.longueur=l
        self.largeur=L
#        on crée les murs et les plateformes dans murs !!!!
        self.murs=[]
        self.portail=None
#       Il faut absolument créer les murs avant de créer les ennemis!!
        self.bombe=[]
        self.robot=[]
        self.missile=Missile(self)
        self.ennemi=self.bombe+self.robot
        
    def creation_mur(self,X,Y,Largeur,Hauteur,type_mur):
        if type_mur=="mur" or type_mur=="Mur"or type_mur=="m" or type_mur=="M":
             self.murs.append(Mur(self,X,Y,Largeur,Hauteur))
        else:
            self.murs.append(Plateforme(self,X,Y,Largeur,Hauteur))
        
    def creation_Bombe(self,X,Y):
        self.bombe.append(Bombe(self,X,Y))
        self.ennemi=self.bombe+self.robot
        
    def creation_Robot(self,mur):
        self.robot.append(Robot(self,mur))
        self.ennemi=self.bombe+self.robot
    
    def creation_Portail(self,X,Y,x,y):
        self.portail=Portail(self,X,Y,x,y)
        
        
    def update(self):
        for mur in self.murs:
            mur.update()
        for rb in self.robot:
            rb.update()
        self.missile.update()
        

        
    

        
