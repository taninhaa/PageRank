import csv 
from tqdm import tqdm
from collections import deque
graphe ={2: {3,4}, 5: {67,85}, 7: {3,4}, 6: {2,5}}

file=open("graphe.txt", "w")

#Fonction qui permet de créer un fichier avec les différentes arêtes d'un dictionnaire
for sommet in graphe: 
    for voisins in graphe[sommet]:
        file.write(str(sommet)+" "+str(voisins)+"\n")

file.close()


