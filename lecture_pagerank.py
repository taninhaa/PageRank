import sys
import numpy as np
import csv

def import_pagerank(fichier):
    id = []
    val_pagerank = []
    with open(fichier, newline='') as csvfile:
        spamreader=csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in spamreader:
            id.append(int(row[0]))
            val_pagerank.append(float(row[1]))

    pagerank = np.array([id,val_pagerank])
    return pagerank

fichier_pagerank = "pagerank.txt"
pagerank = import_pagerank(fichier_pagerank)
index_sort = np.argsort(pagerank[1])

print(np.sort(pagerank[1])[-5:])
