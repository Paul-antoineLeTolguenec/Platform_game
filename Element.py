# -*- coding: utf-8 -*-
"""
Dans ce fichier je définis la super classe Element de laquelle tous les élèment de mon jeu (personnage, mur, ennemis ...) vont hériter
ce qui permet de ne pas répeter le code



"""
import numpy as np
class Element():
    def __init__(self,monde,X,Y,Largeur,Hauteur):
        self._coords=(X,Y)
        self.monde=monde
        self.hauteur=Hauteur
        self.largeur=Largeur
        self._vitesse=(0,0)
        
    def print_element(self):
        pass
   
    def __str__(self):
        print("cet élément évolue dans le monde"+str(self.monde)+"et a pour dimension:"+str(self.largeur)+"x"+str(self.hauteur))
    @property  
    def coords(self):
        return(self._coords)
    @coords.setter
    def coords(self,T):
#        ici je controle les coordonnées pour que les éléments soient toujours dans le monde
        (X,Y)=T
        if X<0:
            X=0
        if X+self.largeur>self.monde.largeur:
            X=self.monde.largeur-self.largeur
            
        if Y<0:
            Y=0
        if Y+self.hauteur>self.monde.longueur:
            Y=self.monde.longueur-self.hauteur
            
        self._coords=(X,Y)
    
    def update(self):
#        méthode d'Euler basique
        dt=0.04 #40 milisec
        (X,Y)=self.coords
        (Xp,Yp)=self._vitesse
        X=dt*Xp+X
        self.coords=(X,Y)


if __name__=="__main__":
    pass