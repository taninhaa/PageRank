from operator import imod
import sys
from graphe_pagerank import reader_lists,pagerank_sparse_perso

liste_ID = []
for ID in sys.argv:
    liste_ID.append(ID)

rows,cols = reader_lists("../data/aretes.txt")
alpha = 1
eps = 10**-6

pi,iter = pagerank_sparse_perso(rows,cols,alpha,eps,liste_ID)
print(pi)