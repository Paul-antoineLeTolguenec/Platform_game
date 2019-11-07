
"""
Ce fichier c0ntient tout les détails en rapport avec mon mur.
on ne redéfinit pas update on utilise celui de élément.
ces objects n'ont pas de fonctions associées ils se définissent par leurs variables d'instances.

@author: letol
"""
from Element import Element
class Mur(Element):
    def __init__(self,monde,X,Y,Largeur,Hauteur):
        super().__init__(monde,X,Y,Largeur,Hauteur)
        self.color="grey"
        self.personnage=None
    

class Plateforme(Element):
    def __init__(self,monde,X,Y,Largeur,Hauteur):
        super().__init__(monde,X,Y,Largeur,Hauteur)
        self.color="dark"
        self.vitesse_mouv=5
        self._vitesse=(self.vitesse_mouv,0)
        
        
    @property
    def coords(self):
        return(self._coords)
    @coords.setter
    def coords(self,T):
         (X,Y)=T
         (Xp,Yp)=self._vitesse
         if X<0:
             X=0
             Xp=self.vitesse_mouv
         if X+self.largeur>self.monde.largeur:
             X=self.monde.largeur-self.largeur
             Xp=-self.vitesse_mouv
            
         if Y<0:
             Y=0
         if Y+self.hauteur>self.monde.longueur:
             Y=self.monde.longueur-self.hauteur
         self._vitesse=(Xp,Yp)
#         print(self._vitesse)
         self._coords=(X,Y)
        
        
    
            
        
    
        

