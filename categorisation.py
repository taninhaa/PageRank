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

def cree_dict():
    size=input("Nombre de catégorie ? :")
    len=int(size)
    dico=dict()
    for i in range(len):
        categorie=input("Nom de la catégorie ? :")
        dico[categorie]=set()
    dico["Autres"]=set()
    return dico

def random_site(site,n):
    id=[]
    tab=[]
    with open(site,'r') as f:
        lines=f.readlines()
        for i in range(n):
            x=random.randint(0,len(lines))
            id.append(x)
            tab.append(lines[x])
    for i in range(n):
        res=''
        condition=0
        for j in tab[i]:
            if(j=='\t'):
                condition=1
            if(j!='\n'  and j!='\t' and condition==1):
                res= res + j
        tab[i]=res
    site=[]
    for i in range(len(tab)):
        site.append((id[i],tab[i]))
    return site

def categorisation(dico,site):
    cat=[]
    for i in dico:
        cat.append(i)
    for i in site:
        print("Pour le site: ",i[1])
        print("Les différentes catégories sont",cat)
        categorie=input("Dans quelle catégorie veux-tu la mettre ? :")
        while(categorie not in dico):
            print("La catégorie n'est pas valide")
            categorie=input("Dans quelle catégorie veux-tu la mettre ? :")
        dico[categorie].add(i[0])
    return dico

def y(categorie,dico):
    if(categorie not in dico):
        return []
    tab=[]
    for i in dico[categorie]:
        tab.append(i)
    return tab

dico=cree_dict()
print("dico",dico)

site=random_site("id-titre.txt",1)
print("site",site)

dico2=categorisation(dico,site)

y=y("Sport",dico2)
print(y)
row,col=reader_lists("aretes.txt")

pr=pr_power_iteration_sparse(row,col,0.85,1e-10,True,y)
print(pr)