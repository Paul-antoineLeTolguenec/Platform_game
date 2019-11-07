# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:22:01 2019

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

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QKeyEvent,QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

class Fenetre(QWidget,Thread):
    def __init__(self,personnage):
        QWidget.__init__(self)
        Thread.__init__(self)
        self.setWindowTitle("Portail")
        self.resolution=10 #pixels par mètre

        self.setFixedSize(personnage.monde.largeur*self.resolution, personnage.monde.longueur*self.resolution+50)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(410, 810, 551, 351))
        self.conteneur.setObjectName("conteneur")
        self.widget = QtWidgets.QWidget(self.conteneur)
        self.widget.setGeometry(QtCore.QRect(40, 110, 366, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bouton= QPushButton(self.widget)
        _translate = QtCore.QCoreApplication.translate
        self.bouton.setText(_translate("Portail", "Start"))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(170, 100, 700, 700))
        self.conteneur.setObjectName("conteneur")
        self.widget = QtWidgets.QWidget(self.conteneur)
        self.widget.setGeometry(QtCore.QRect(40, 110, 700, 700))
        self.widget.setObjectName("widget")
        
        self.etat_jeu="off"
        # on connecte le signal "clicked" a la methode appui_bouton
        self.bouton.clicked.connect(self.clique_start)
        # creation du gestionnaire de mise en forme
#        self.setStyleSheet(" background-color: red");
        self.personnage=personnage
        self.x=10
    
    def clique_start(self):
        self.etat_jeu="on"
        self.bouton.setEnabled(False)
            
    def paintEvent(self,e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawPixmap(0, 0, QPixmap("galaxy.jpg"))
        qp.setPen(Qt.black)
        (X,Y)=self.personnage.coords
        Y=-Y*self.resolution-self.personnage.hauteur*self.resolution+self.resolution*self.personnage.monde.longueur

        qp.drawPixmap(X*self.resolution,Y,self.personnage.largeur*self.resolution,self.personnage.hauteur*self.resolution,QPixmap("personnage.png"))
#        on dessine les murs
        for mur in self.personnage.monde.murs:
            (xmur,ymur)=mur.coords
            ymur=-ymur*self.resolution-mur.hauteur*self.resolution+self.resolution*self.personnage.monde.longueur
            xmur=xmur*self.resolution
            qp.drawPixmap(xmur,ymur,mur.largeur*self.resolution,mur.hauteur*self.resolution,QPixmap("mur.png"))
#        on dessine les ennemis
        for ennemis in self.personnage.monde.bombe:
            (xen,yen)=ennemis.coords
            yen=-yen*self.resolution-ennemis.hauteur*self.resolution+self.resolution*self.personnage.monde.longueur
            xen=xen*self.resolution
            qp.drawPixmap(xen,yen,ennemis.largeur*self.resolution,ennemis.hauteur*self.resolution,QPixmap("bombe.png"))
            
        for ennemis in self.personnage.monde.robot:
            (xen,yen)=ennemis.coords
            yen=-yen*self.resolution-ennemis.hauteur*self.resolution+self.resolution*self.personnage.monde.longueur
            xen=xen*self.resolution
            qp.drawPixmap(xen,yen,ennemis.largeur*self.resolution,ennemis.hauteur*self.resolution,QPixmap("robot.jpg"))
#        on dessine le missile. Je le met a part parce que je l'ai fait en dernier.
#        je print aussi le lanceur de missile qui sert pas à grand chose mise à part 
        qp.drawPixmap(self.personnage.monde.largeur*self.resolution-100,0,100,100,QPixmap("lanceur.png"))
        (x,y)=self.personnage.monde.missile.coords
        y=-y*self.resolution-self.personnage.monde.missile.hauteur*self.resolution+self.resolution*self.personnage.monde.longueur
        x=x*self.resolution
        qp.drawPixmap(x,y,self.personnage.monde.missile.largeur*self.resolution,self.personnage.monde.missile.hauteur*self.resolution,QPixmap("missile.png"))
#        on dessine le portail
        if self.personnage.monde.portail.portail_etat=="open":
            qp.setPen(Qt.blue)
            (xportail,yportail)=self.personnage.monde.portail.coords
            yportail=-yportail*self.resolution-self.personnage.monde.portail.hauteur*self.resolution+self.resolution*self.personnage.monde.longueur
            qp.drawPixmap(xportail*self.resolution,yportail,self.personnage.monde.portail.largeur*self.resolution,self.personnage.monde.portail.hauteur*self.resolution,QPixmap("porte.png"))
#        et la cle:
        if self.personnage.monde.portail.portail_etat!="open":
            (xcle,ycle)=self.personnage.monde.portail.cle.coords
            ycle=-ycle*self.resolution-self.personnage.monde.portail.cle.hauteur*self.resolution+self.resolution*self.personnage.monde.longueur
            qp.drawPixmap(xcle*self.resolution,ycle,self.personnage.monde.portail.cle.largeur*self.resolution,self.personnage.monde.portail.cle.hauteur*self.resolution,QPixmap("clé.png"))
        if self.personnage.etat_perso=="mort":
            im=QtGui.QImage("Image1.png")
            qp.drawImage(250,370,im)
        if self.personnage.etat_jeu=="gagné":
            im1=QtGui.QImage("logo.png")
            qp.drawImage(0,200,im1)
            
        
            
        qp.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            print(self.width())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            self.personnage.sauter()
        elif e.key() == Qt.Key_Left:
            self.personnage.aller_gauche()
        elif e.key() == Qt.Key_Right:
            self.personnage.aller_droite()
            
    def closeEvent(self,QCloseEvent):
        self.etat_jeu="on"

        