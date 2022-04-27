import networkx as nx
import data2py as data


     
G = nx.Graph()     
name1 = data.regular_path1.split(" N ")
name2= data.regular_path2.split(" N ")

def Creategraphe():
    for i in range(len(name1)-1):
        G.add_edge(name1[i], name1[i+1], poids = 1)
      
        for i in range(len(name2)-1):
            G.add_edge(name2[i], name2[i+1], poids = 1)



      
      
#==============================================================
      #fonction sur les horraires sources internet
#==============================================================
    
#remplace h:min en sec
def Horraire_Seconde(time):
    h_splited = time.split(":")
    heures = int(h_splited[0])*60        
    minutes = int(h_splited[1])
    temps = heures + minutes
    return temps

#remplace sec en h:min
def Horraire_minute(time):
    heure = time // 60
    minute = time % 60
    return (heure,minute)

#convertit toutes les horaires des fichiers en secondes
def conversionHorairesgo():
    for elem in data.regular_date_go[0]:
        print(elem)
        liste=[]
        for j in data.regular_date_go[0][elem]:
            if j == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(j))
                
        print(liste, end =",")
        print("\n")
        
    for elem in data.regular_date_go[1]:    
        print(elem)
        liste=[]
        for j in data.regular_date_go[1][elem]:
            if j == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(j))
       
        print(liste, end =",")
        print("\n")
        
        
#==============================================================
      #trouve le prochain bus qui passe a un arret donné
#==============================================================
    
        

def ProchainBus(heure, ligne, depart, direction, we):
    if ligne == "1" and direction == "LYCEE_DE_POISY + POISY_COLLEGE" and we=="n" :
        path = data.regular_date_back
    elif ligne == "1" and direction == "LYCEE_DE_POISY + POISY_COLLEGE" and we=="o" :
        path = data.we_holidays_date_back
    elif ligne == "1" and direction == "PARC_DES_GLAISINS" and we=="n" :
        path = data.regular_date_go
    elif ligne == "1" and direction == "PARC_DES_GLAISINS" and we=="o" :
        path = data.we_holidays_date_go
    elif ligne == "2" and direction == "PISCINE-PATINOIRE" and we=="n" :
        path = data.regular_date_back
    elif ligne == "2" and direction == "PISCINE-PATINOIRE" and we=="o" :
        path = data.we_holidays_date_back
    elif ligne == "2" and direction == "CAMPUS" and we=="n" :
        path = data.regular_date_go
    elif ligne == "2" and direction == "CAMPUS" and we=="o" :
        path = data.we_holidays_date_go

    liste=[]
    hor=Horraire_Seconde(heure)
    if ligne == "1" :
        for heure in path[0][depart]:
            if heure == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(heure))
        for elem in liste:
            if type(elem) != str:
                if (elem - hor > 0):
                    return Horraire_minute(elem)
    
    if ligne == "2":
        for heure in path[1][depart]:
            if heure == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(heure))
        for elem in liste:
            if type(elem) != str:
                if (elem - hor > 0):
                    return Horraire_minute(elem) 
#==============================================================
      #Algo 
#==============================================================                 

#le chemin le plus rapide 
      
def shortest(depart, arrive):
    print("le chemin le plus court est : ", nx.shortest_path(G,depart,arrive))
    
def fastest(depart, arrive):
    print("le chemin le plus rapide est : ", nx.fastest_path(G,depart,arrive))
    
def foremost(depart, arrive):
    print("le chemin le plus rapide est : ", nx.formost_path(G,depart,arrive))
    


while True:
    Creategraphe()
    heure = input("Quelle heure est-il? \n")
    ligne = input("Sur quelle ligne êtes vous ? \n")
    depart = input("A quel arrêt vous trouvez vous? \n")
    arrive = input("A quel arrêt vous voulez allez ? \n ")
    direction = input("quelle est votre direction ? \n ")
    we = input("weekend ? o/n")
    print("votre prochain bus est à : ", ProchainBus(heure, ligne, depart, direction, we))
    print("le chemin le plus court est : ", nx.shortest_path(G, depart, arrive))
    print("le chemin le plus rapide est:", nx.fastest_path(G, depart, arrive))
    print("le chemin qui arrive le plus tôt est :", nx.foremost_path(G,depart,arrive))
    
    break






