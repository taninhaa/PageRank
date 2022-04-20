import csv 
import time
import scipy
""" Fonction qui permet de lire un fichier d'aretes et de créer le dictionnaire correspondant"""
#Graphe 
def conversion_dict_fichier_graphe(fichier):
    lignes=[]
    colonnes=[]
    with open(fichier, newline='') as csvfile:
        
        for row in csv.reader(csvfile, delimiter=' ', quotechar='|'):
            lignes.append(row[0]) 
            colonnes.append(row[1])
                
#Affiche le graphe
t1 = time.time()
conversion_dict_fichier_graphe('soc-buzznet.mtx')
t2 = time.time()
print(t2-t1)
"""
for i in graphe1.items():
    print(i) """
