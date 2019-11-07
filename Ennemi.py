# -*- coding: utf-8 -*-
"""
dans ce fichier je vais créer toute les différentes classes d'ennemis que va comporter le jeu.
Il y a 3 classes:
    -bombe
    -robot
    -missile
Chaque objet aura une façon d'interagir avec le personnage de mon jeu.
donc une méthode pour se déplacer et toucher le personnage.
Petite spécificité pour missile.
Dans la version que j'ai crée de missile. Le missile se lance obligatoirement du coin en haut à gauche du monde. 
@author: letol
"""
from Element import Element
#from Simulation import Simulation
import numpy as np
        

#dans la classe est exactement comme un ennemi mais il s'agit d'un cube de couleur rouge et de dimenssion 3 par 3   
class Bombe(Element):
    def __init__(self,monde,X,Y):
        super().__init__(monde,X,Y,1,1)
        self.couleur="red"

class Robot(Element):
#    les robot sont des ennemis stationnaire jusqu'à ce que le bonhomme passe sur la même horizontale que lui et il lui fonce dessus
     def __init__(self,monde,mur):
        (xmur,ymur)=mur.coords
        super().__init__(monde,xmur,ymur+mur.hauteur,1,1)#j'initialise les coordonnées du robot sur le mur
        self.couleur="blue"
        self._vitesse=(0,0)
        self.speed_focus=13
        self.mur=mur
        
     @property 
     def coords(self):
        return(self._coords)
     @coords.setter
     def coords(self,T):
         (X,Y)=T
         (xmur,ymur)=self.mur.coords
         if X<0:
             X=0
             self._vitesse=(0,0)
         elif X+self.largeur>self.monde.largeur:
             X=self.monde.largeur-self.largeur
             self._vitesse=(0,0)
            
         if Y<0:
             Y=0
         elif Y+self.hauteur>self.monde.longueur:
             Y=self.monde.longueur-self.hauteur
#        je m'occupe maintenant des cotés du mur
         if X<xmur:
             X=xmur
             self._vitesse=(0,0)
         elif X+self.largeur>xmur+self.mur.largeur:
             X=xmur+self.mur.largeur-self.largeur
             self._vitesse=(0,0)
             
         self._coords=(X,Y)
    
     
     
     
     
     def poursuivre(self,side):
         if side=="droite":
             self._vitesse=(self.speed_focus,0)
         else:
             self._vitesse=(-self.speed_focus,0)
         
#les missiles seront toujours lancés depuis le coin en haut droit de la map
#Je pourrais les lancer d'ou je veux mais dans le jeu dont je m'inspire ils se lancent comme ça
   
class Missile(Element):

    def __init__(self,monde):
        super().__init__(monde,monde.largeur-1,monde.longueur-1,1,1)#j'initialise à chaque fois le missile dans le coin en haut à gauche de la map
        self._vitesse=(0,0)
        self.speed_focus=6
    
    def toucher(self,element): #je crée la fonction toucher qui prend en argument n'importe quelle chose et qui renvoie true si le missile touche cette chose
        (xel,yel)=element.coords
        (X,Y)=self.coords
        if Y<yel+element.hauteur and Y+self.hauteur>yel and X+self.largeur>xel and X<xel:
            return(True)
        elif Y<yel+element.hauteur and Y+self.hauteur>yel and X<xel+element.largeur and X>xel:
            return(True)
        elif X+self.largeur>xel and X<xel+element.largeur and Y<yel+element.hauteur and Y>yel:
            return(True)
        elif X+self.largeur>xel and X<xel+element.largeur and Y+self.hauteur>yel and Y<yel:
            return(True)
        else:
            return(False)
        
    @property 
    def coords(self):
        return(self._coords)
     
    @coords.setter
    def coords(self,T):
         (X,Y)=T
         if X<0:
            X=0
         if X+self.largeur>self.monde.largeur:
            X=self.monde.largeur-self.largeur
            
         if Y<0:
            Y=0
         if Y+self.hauteur>self.monde.longueur:
            Y=self.monde.longueur-self.hauteur
         for mur in self.monde.murs:
            if self.toucher(mur):
                (X,Y)=(self.monde.largeur-1,self.monde.longueur-1)
         self._coords=(X,Y)
         
    def poursuivre(self,angle):
#        cette fonction sera toujours éxecutée dans le setter des coordonnées de personnage. Elle permet d'orienter la vitesse du missile pour qu'il se dirige vers le bonhomme.
        Xp=self.speed_focus*np.cos(angle)
        Yp=self.speed_focus*np.sin(angle)
        self._vitesse=(Xp,Yp)
   
    def update(self):
        dt=0.04 #40 milisec
        (X,Y)=self.coords
        (Xp,Yp)=self._vitesse
        X=dt*Xp+X
        Y=dt*Yp+Y
        self.coords=(X,Y)


         
    
    
    
        
            
        
        
    
        