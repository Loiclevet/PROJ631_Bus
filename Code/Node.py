

class node():
    
    def __init__(self, name, avant=[], apres=[], ligne=[]):
        self.name = name
        self.avant = avant
        self.apres = apres
        self.ligne = ligne
        
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