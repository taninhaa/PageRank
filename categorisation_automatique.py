import random
import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
import scipy.sparse as sps
import scipy.sparse.linalg as spl
import seaborn
import sys
import csv

sys.path.append("./fonctions")
from read_file_into_row_col import reader_lists
from pr_power_iteration_sparse import pr_power_iteration_sparse
from categorisation import creation_dict_titre, cree_dict
from categorisation import random_site
from categorisation import cree_dict_vide
from categorisation import categorisation_manuelle
from categorisation import liste

def categorisation_automatique(n):
    rows,cols=reader_lists("aretes.txt")
    dico_entier=cree_dict()
    site=random_site("id-titre.txt",n)
    dico_categorie=categorisation_manuelle(dico_entier,site)

    dico_final=creation_dict_titre("id-titre.txt")
    resultat=dict()
    for cle in dico_categorie:
        liste_perso=liste(dico_entier,dico_categorie,cle)
        pr=pr_power_iteration_sparse(rows,cols,0.85,1e-10,True,liste_perso)
        resultat[cle]=pr
    
    i=0
    for titre in dico_final:
        categorie_max=0
        valeur_max=0
        for cle in resultat:
            if(resultat[cle][i]>valeur_max):
                valeur_max=resultat[cle][i]
                categorie_max=cle
        for cle2 in dico_entier:
            if categorie_max==dico_entier[cle2]:
                categorie_str=cle2
        dico_final[titre]=categorie_str
        i=i+1
    file=open("categorie.csv","w")
    writer = csv.writer(file)
    for key, value in dico_final.items():
        writer.writerow([key, value])

    file.close()
    return dico_final

dico=categorisation_automatique(5)