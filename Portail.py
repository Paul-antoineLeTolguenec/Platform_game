# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:57:36 2019
le personnage doit d'abord aller chercher la clé et ensuite entrer dans le portail

@author: letol
"""
from Element import Element
class Portail(Element):
    def __init__(self,monde,X,Y,x,y):
        super().__init__(monde,X,Y,3,3)
        self.cle=Element(monde,x,y,3,3) #ici on rentre les coordonnées de la clé
       #la clé ouvrant le portail fera 1m sur 1m
        self.couleur_key="green"
        self.couleur_portail="grey"
        self.portail_etat="close"
        self.portail_traverse=0 #ça va me renseigner si le personnage a traversé le portail ou non 
        
        
    def ouvre_le_portail(self):
        self.portail_etat="open"
        self.couleur_portail="blue"
    
    def gagner(self):
        print("you won !!!!")
        
        
    
        