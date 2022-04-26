# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:40:02 2022

@author: levetl
"""

from ligne import Lignes
import data2py as data

class Arret(Lignes):
    
    def __init__ (self, direction, nom, numLigne=[], horaires=[]):
    
        self.horaires = horaires
        self.direction = direction
        self.nom = nom
        self.numLigne = numLigne

    
    def getDirection(self):
        return self.direction
    
    def getNom(self):
        return self.nom
    
    def getLigne(self, ligne1:Lignes):
      liste= ligne1.getArret()
      for nomArret in liste:
          if nomArret == self.nom:
              self.numLigne = ligne1.numero
              return self.numLigne
            
             
    def getHoraireAller(self):
        self.horaires = data.regular_date_go[self]
        return self.horaires
            
    def getHoraireRetour(self, ligne:Lignes):
        nom = ligne.getArret()
        for name in nom:
            if self.getNom() == name:
                self.horaires = data.regular_date_back[name]
        return self.horaires