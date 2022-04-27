import data2py as data



class Lignes ():
    def __init__(self, numero, arret=[]):
        self.numero = numero
        self.arret = arret 
        
        
    def getArret(self):
        name = data.regular_path.split(" N ")
        for a in name:
            self.arret.append(a) 
        return self.arret
    
    def getNumero(self):
        return self.numero
    

    
    
