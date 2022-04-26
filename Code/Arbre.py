# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:01:43 2022

@author: levetl
"""

from Node import node
    
class arbre(node):
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def setNodes(self):
        pass           
    
    
# On va alors implémenter tous les arrêts des deux lignes
# pour plus de simplicité on écrira les arrêts en MAJUSCULE
        
    
"""LIGNE N°1 POSY - PARC DES GLAISINS"""


node1A=node('LYCÉE_DE_POISY')
node1B=node('POISY COLLEGE')
node1C=node('VERNOD')
node1D=node('MEYTHET LE RABELAIS')
node1E=node('CHORUS')
node1F=node('MANDALLAZ')
node1G=node('GARE')
node1H=node('FRANCE BARATTES')
node1I=node('C.E.S BARATTES')
node1J=node('VIGNIERES')
node1K=node('PONCHY')
node1L=node('PARC DES GLAISINS')



"""LIGNE N°2 PISCINE/PATINOIRE - CAMPUS"""


node2A=node('PISCINE PATINOIRE')
node2B=node('ARCADIUM')
node2C=node('PARC DES SPORTS')
node2D=node('PLACE DES ROMAINS')
node2E=node('COURIER')
node2F=node('GARE')
node2G=node('BONLIEU')
node2H=node('PREFECTURE PAQUIER')
node2I=node('IMPERIAL')
node2J=node('POMMARIES')
node2K=node('VIGNIERES')
node2L=node('CAMPUS')



"""""ON PARAMETRE LES ARRETS PRECEDANT & SUIVANT"""""

node1A.setApres(node1B)

node1B.setAvant(node1A)
node1B.setApres(node1C)

node1C.setAvant(node1B)
node1C.setApres(node1D)

node1D.setAvant(node1C)
node1D.setApres(node1E)

node1E.setAvant(node1D)
node1E.setApres(node1F)

node1F.setAvant(node1E)
node1F.setApres(node1H)

node1G.setAvant(node1F)
node1G.setApres(node1H)

node1H.setAvant(node1G)
node1H.setApres(node1I)

node1I.setAvant(node1H)
node1I.setApres(node1J)

node1J.setAvant(node1I)
node1J.setApres(node1K)

node1K.setAvant(node1J)
node1K.setApres(node1L)


""""""""""""""""""""""""""""""""""""""""""""""""""""""

node2A.setApres(node2B)

node2B.setAvant(node2A)
node2B.setApres(node2C)

node2C.setAvant(node2B)
node2C.setApres(node2D)

node2D.setAvant(node2C)
node2D.setApres(node2E)

node2E.setAvant(node2D)
node2E.setApres(node2F)

node2F.setAvant(node2E)
node2F.setApres(node2H)

node2G.setAvant(node2F)
node2G.setApres(node2H)

node2H.setAvant(node2G)
node2H.setApres(node2I)

node2I.setAvant(node2H)
node2I.setApres(node2J)

node2J.setAvant(node2I)
node2J.setApres(node2K)

node2K.setAvant(node2J)
node2K.setApres(node2L)


string = ''
for i in node1C.getApres():
    string += i
print(string)









