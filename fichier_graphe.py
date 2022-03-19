import csv 
from tqdm import tqdm
from collections import deque
graphe1 ={2: {3,4}, 5: {67,85}, 7: {3,4}, 6: {2,5}}

def conversion_dict_fichier(fichier, graphe):
    file=open(fichier, "w")

    #Fonction qui permet de créer un fichier avec les différentes arêtes d'un dictionnaire
    for sommet in graphe: 
        for voisins in graphe[sommet]:
            #file.write(str(sommet)+" "+str(voisins)+"\n")
            file.write("%d\t%d\n"%(sommet,voisins))
    file.close()


conversion_dict_fichier("graphe.txt", graphe1)
