import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
import scipy.sparse as sps
import scipy.sparse.linalg as spl
import seaborn
import sys
import csv
sys.path.append("../fonctions")
from creation_dict  import dico_construction

"""rows,cols=reader_lists("aretes.txt")
dico=dico_construction(rows,cols)
pr_exact=exact_pr(rows,cols,0.85)

print(pagerank_sparse(rows,cols,0.85,1e-10))

print(forward_push(dico,0.85,1e-10,pr_exact))"""
