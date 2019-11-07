# -*- coding: utf-8 -*-
"""
Dans ce fichier, je crée ma classe Personnage. 
Le jeu portal est un jeu arcade donc en étroit lien avec 
une interface graphique .
Donc mon personnage sera doté de coordonnées et d'une hauteur, largeur qui seront fixé.
Aussi pour comprendre mes choix de coordonnées, je précise 
que le bonhomme évolue dans un monde que j'aurai crée dans une autre classe.
Descriptif de Personnage:
    les coordonnées:
        je considère que chaque élèment de mon monde se définit par des coordonées.
        ces coordonées sont les coordonées en bas à gauche de l'élèment.
        C'est à dire que je choisis un point de mon personnage(qui est sont point de plus petit x et y) et je me repère avec ce point.
        La largeur et la hauteur sont des élèments qui me permettent de gérer l'espace au tour du bonhomme.
        
    

@author: letol
"""
import numpy as np
from Monde import Monde
from Mur import Mur
from Element import Element

class Personnage(Element):
    def __init__(self,monde,X,Y,Largeur,Hauteur):
        super().__init__(monde,X,Y,Largeur,Hauteur)
        self._vitesse=(0,0)
        self.acceleration=(0,0)
        self.masse=80
        self.poids=9.81*self.masse
        self.acceleration_mouv=100
        self.vitesse_saut_mur=5
        self.vitesse_saut=14.5
        self.frottement=200
        self.frottement_sol=self.frottement
        self.vitesse_max_x=20
        self.vitesse_max_y=15
        self.vitesse_dep=5
        self.etat_perso="vivant"
        self.temps_vie=3*60
        self.etat_jeu="en cours"# vie en minute
  
#Dans cette partie je gère l'affectation des coordonnées du perso pour
#qu'il ne sorte pas de la map ou qu'il ne rentre pas dans les murs 
     
    @property
    def coords(self):
        return(self._coords)
        
    @coords.setter   
    def coords(self,T):
        (X,Y)=T
        (Xp,Yp)=self.vitesse
        (Xpp,Ypp)=self.acceleration
#   Vérification si le perso est bien dans le monde 
#        Pour l'abscisse 
        if X<0:
            X=0
            if Xp<0:
                Xp=0
                Xpp=0
        elif X+self.largeur>self.monde.largeur:
            X=self.monde.largeur-self.largeur
            if Xp>0:
                Xp=0
                Xpp=0
#        Pour l'ordonnée
        if Y<0:
            self.frottement_sol=self.frottement
            Y=0
            if Yp<0:
                Yp=0
                Ypp=0
        elif Y>0:
            Ypp=-self.poids/self.masse
            self.frottement_sol=0
        else:
            self.frottement_sol=self.frottement
          

#   Vérification des Murs du Monde:
        for mur in self.monde.murs:
            (xmur,ymur)=mur.coords
#          je vérifie les cotés du bonhomme
            if X>xmur-self.largeur and X<xmur+mur.largeur and Y<ymur+mur.hauteur and Y>ymur+mur.hauteur-self.hauteur/2: #on a eu un petit problème ladessus
#                si contact en bas
                Y=ymur+mur.hauteur
                self.frottement_sol=self.frottement
                Yp=0
                Ypp=0
                
            elif X>xmur-self.largeur and X<xmur+mur.largeur and Y+self.hauteur>ymur and Y+self.hauteur<ymur+0.5:
#                en haut
                Y=ymur-self.hauteur
                self.frottement_sol=self.frottement
                Yp=0
                Ypp==-self.poids/self.masse
                
                    
                
            elif Y>ymur-self.hauteur and Y<ymur+mur.hauteur and X>xmur-self.largeur and X<xmur:
#                si contact à droite :
                X=xmur-self.largeur
                self.frottement_sol=self.frottement
#                if Xp>0: # le perso doit s'éloigner du mur
                Xp=0
                Xpp=0
#                si contact à gauche
            elif Y>ymur-self.hauteur and Y<ymur+mur.hauteur and X<(xmur+mur.largeur) and X>xmur:
                X=xmur+mur.largeur
                self.frottement_sol=self.frottement
#                if Xp<0:
                Xp=0
                Xpp=0
#            else: #si il n'est pas en contact avec un mur, il est dans le vide et donc l'accélération est la pesanteur
#                Ypp=-self.poid/self.masse
#           

#             Maintenant on va vérifier pour les ennemis
#            si les bombes et les robots tuent le perso
        for ennemi in self.monde.ennemi:
            if self.toucher(ennemi):
                self.mourir()
                break
        if self.toucher(self.monde.missile):
            self.mourir()

                    
                    
                    
                    
#            Si les robots doivent bouger (def track)
        for robot in self.monde.robot:
            if self.horizontal(robot)=="droite":
                robot.poursuivre("droite")
                    
            elif self.horizontal(robot)=="gauche":
                robot.poursuivre("gauche")
                
#        je programme maintenant la track du missile sur le bonhomme:
        (xmissile,ymissile)=self.monde.missile.coords
        if X-xmissile<0:
            try:
                angle=np.arctan((Y-ymissile)/(X-xmissile))+np.pi
            except:
                angle=np.arctan((Y-ymissile)/((X-xmissile)+1))+np.pi

        else:
            try:
                angle=np.arctan((Y-ymissile)/(X-xmissile))
            except:
                angle=np.arctan((Y-ymissile)/((X-xmissile)+1))

                

            
        self.monde.missile.poursuivre(angle)
        
        
                    
                    
#            On va vérifier pour le portail
        if self.toucher(self.monde.portail.cle):
            self.monde.portail.portail_etat="open"
            self.monde.portail.couleur_portail="blue" # ici j'ouvre le portail si le bonhomme touche la cle
           
        if self.monde.portail.portail_etat=="open"and self.toucher(self.monde.portail):
            self.gagner() # ici le bonhomme gagne s'il touche le portail et qu'il est ouvert
         
        self._coords=(X,Y)
        self.vitesse=(Xp,Yp)
        self.acceleration=(Xpp,Ypp)
        
        
        
        
        
        
    
    @property
    def vitesse(self):
        return(self._vitesse)
    @vitesse.setter
    def vitesse(self,T):
        (Xp,Yp)=T
#        Controle de la vitesse
        if Xp>self.vitesse_max_x:
            Xp=self.vitesse_max_x
        elif Xp<-self.vitesse_max_x:
            Xp=-self.vitesse_max_x
        if Yp<-self.vitesse_max_y:
            Yp=-self.vitesse_max_y
        self._vitesse=(Xp,Yp)
    
    def horizontal(self,element): # cette fonction va retourner le coté vers lequel les robots vont devoir tracker le bonhomme:
        (xel,yel)=element.coords
        (X,Y)=self.coords
        if Y<yel+element.hauteur and Y+self.hauteur>yel and X>xel:
            return("droite")
        elif Y<yel+element.hauteur and Y+self.hauteur>yel and X<xel:
            return("gauche")
        else:
            return("")
    def toucher(self,element): #je crée la fonction toucher qui prend en argument n'importe quelle chose et qui renvoie true si le bonhomme touche cette chose
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
            
        
    def mourir(self):
        self.etat_perso="mort"
        
    
    
    
    def gagner(self):
        self.etat_jeu="gagné"
            
        
    
#Ensuite je crée une fonction qui me permet de savoir si le personnage est sur un socle ou dans le vide
#elle renvoie True si le perso est sur un socle false sinon

    def sur_le_sol(self):
        (X,Y)=self.coords
        v=0
        if Y!=0:
            for mur in self.monde.murs:
                (xmur,ymur)=mur.coords
#               procédure pour les murs ou modules rectangulaires
                if ymur+mur.hauteur==Y and X>xmur and X<(xmur+mur.largeur):
                    v=1
                    break
            if v==1:
                return(True)
            else:
                return(False)
        else:
            return(True)
            
# je crée une fonction permettant de déterminer si le bonhomme glise le long d'un mur:
    def touche_le_mur(self):
        (X,Y)=self.coords
        side=""
        #Les cotés de la map
        if X==0:
            side="left"
        elif X+self.largeur==self.monde.largeur:
            side="right"
        for mur in self.monde.murs:
            (xmur,ymur)=mur.coords
            if X==xmur+mur.largeur:
                side="left"
                break
            elif X+self.largeur==xmur:
                side="right"
                break
        return(side)
            
                   
                    
                
#Ici je définis les fonctions de mouvements du personnage
#Pour l'instant le robot se déplace de façon très archaïque mais ces fonctions ne pourront être changées que lors de la mise en place
#de l'espace graphique.

    def aller_droite(self):
        (Xpp,Ypp)=self.acceleration
        (Xp,Yp)=self.vitesse
        Xpp=self.acceleration_mouv
        Xp=Xp+self.vitesse_dep
        self.acceleration=(Xpp,Ypp)
        self.vitesse=(Xp,Yp)
       
    def aller_gauche(self):
        (Xpp,Ypp)=self.acceleration
        (Xp,Yp)=self.vitesse
        Xpp=-self.acceleration_mouv
        Xp=Xp-self.vitesse_dep
        self.acceleration=(Xpp,Ypp)
        self.vitesse=(Xp,Yp)
    
    def sauter(self):
        (Xp,Yp)=self.vitesse
        if self.sur_le_sol()==True: # je ne permets le saut que si mon bonhomme est sur un mur
            Yp=self.vitesse_saut
            self.vitesse=(Xp,Yp)
        elif self.touche_le_mur()=="right":
            Yp=self.vitesse_saut
            Xp=-self.vitesse_saut_mur
            self.vitesse=(Xp,Yp)
        elif self.touche_le_mur()=="left" :
            Yp=self.vitesse_saut
            Xp=self.vitesse_saut_mur
            self.vitesse=(Xp,Yp)
           
   
#'''si le temps me le permet je mettrais en place une approche plus physique du jeu avec la résolution d'un PFD grace à Euler.'''
    def update(self):
        dt=0.04 #40 milisec
        (Xpp,Ypp)=self.acceleration
        (Xp,Yp)=self.vitesse
        (X,Y)=self.coords
        Xp=dt*Xpp+Xp
        Yp=dt*Ypp+Yp
        Xpp=-((self.frottement_sol)/(self.masse))*Xp
        X=dt*Xp+X
        Y=dt*Yp+Y
        self.vitesse=(Xp,Yp)
        self.acceleration=(Xpp,Ypp)
#'''Le self .coords doit être mis en dernier car c'est la fonction qui vérifie le plus de choses'''
        self.coords=(X,Y)
        
if __name__=="__main__":
    pass

                    
            
                        
                        
            
