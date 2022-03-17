# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:30:03 2022

@author: levetl
"""

class node():
    
    def __init__(self, name, avant=[], apres=[], ligne=[]):
        self.name = name
        
    ## on réalise les setteur
    
    def setAvant(self, av):
        self.avant.append(av)
        
    def setApres(self, ap):
        self.apres.append(ap)
        
        
    ## On réalise les getteur 
    
    def getName(self):
        return self.name
    
    def getAvant(self):
        liste = []
        for av in self.avant :
            liste += av.getName()
        return liste
    
    def getApres(self):
        liste = []
        for ap in self.apres :
            liste += ap.getName()
        return liste    
    
    def getLigne(self):
        return self.ligne
    
    def __str__(self):
        return self.name