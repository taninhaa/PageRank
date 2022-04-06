import csv
import time
from graphe_pagerank import pagerank_sparse
from graphe_pagerank import pagerank_sparse_perso
import numpy as np
import sys

def conversion_list_fichier_graphe(fichier):
    print(fichier)
    ligne =[]
    colonne = []
    with open(fichier, newline='') as csvfile:
        spamreader=csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in spamreader:
            ligne.append(int(row[0]))
            colonne.append(int(row[1]))

    return ligne,colonne

def export_pagerank(fichier,pagerank):
    with open(fichier,"w") as file:
        for i in range(pagerank.size):
            file.write("%d\t%.15f\n"%(i+1,pagerank[i]))

#Lecture du fichier d'arêtes
fichier_aretes = "./aretes.txt"
t1 = time.time()
(ligne,colonne) = conversion_list_fichier_graphe(fichier_aretes)
t2 = time.time()
print(t2-t1)

#Calcul du pagerank
#page_rank = pagerank_sparse(ligne,colonne,0.85,0.000001)

def ligne_personnalise(id):
    ligne_perso=[]
    with open("aretes.txt", newline='') as csvfile:
        spamreader=csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in spamreader:
            if id==int(row[0]):
                ligne_perso.append(int(row[1]))

    return ligne_perso
            
lignes=ligne_personnalise(0)
#print(lignes)
page_rank,it=pagerank_sparse_perso(ligne,colonne,0.85,1e-10,lignes)
print(page_rank)
#Export du pagerank dans un fichier
#fichier_pagerank = "pagerank.txt"
#export_pagerank(fichier_pagerank,page_rank)