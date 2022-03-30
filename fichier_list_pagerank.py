import csv
import time
from graphe_pagerank import pagerank_sparse
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
page_rank = pagerank_sparse(ligne,colonne,0.85,0.000001)

#Export du pagerank dans un fichier
fichier_pagerank = "pagerank.txt"
export_pagerank(fichier_pagerank,page_rank)