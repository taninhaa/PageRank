import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
import scipy.sparse as sps
import scipy.sparse.linalg as spl
import seaborn
import csv
import sys

sys.path.append("/PageRank/graphe_pagerank.py")

from graphe_pagerank import reader_lists


"""rows,cols=reader_lists("aretes.txt")
dico=dico_construction(rows,cols)
pr_exact=exact_pr(rows,cols,0.85)

print(pagerank_sparse(rows,cols,0.85,1e-10))

print(forward_push(dico,0.85,1e-10,pr_exact))"""
