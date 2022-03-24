import csv
import time
from graphe_pagerank import pagerank_sparse
def conversion_list_fichier_graphe(fichier):
    ligne =[]
    colonne = []
    with open(fichier, newline='') as csvfile:
        spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            ligne.append(int(row[0]))
            colonne.append(int(row[1]))

    return ligne,colonne

t1 = time.time()
(ligne,colonne) = conversion_list_fichier_graphe("graphe.txt")
t2 = time.time()
print(t2-t1)
for i in range(5):
    print(ligne[i],colonne[i])

page_rank=pagerank_sparse(ligne,colonne,0.85,0.000001)
print(page_rank)