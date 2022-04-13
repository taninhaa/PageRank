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

def liste(categorie,dico):
    if(categorie not in dico):
        return []
    tab=[]
    for i in dico[categorie]:
        tab.append(i)
    return tab
"""
dico=cree_dict()
print("dico",dico)

site=random_site("id-titre.txt",1)
print("site",site)

dico2=categorisation(dico,site)

liste=liste("Sport",dico2)
print(liste)
row,col=reader_lists("aretes.txt")"""

#pr=pr_power_iteration_sparse(row,col,0.85,1e-10,True,y)
#print(pr)

def cree_dict2():
    size=input("Nombre de catégorie ? :")
    len=int(size)
    dico=dict()
    for i in range(len):
        categorie=input("Nom de la catégorie ? :")
        dico[categorie]=i
    dico["Autres"]=len
    return dico



def cree_dict3(size):
    dico=dict()
    for i in range(size):  
        dico[i]=set()
    return dico



def categorisation2(dico,site):
    print("Les différentes catégories sont")
    print(dico)
    print("Rentrez l'entier associé")
    dico_c=cree_dict3(len(dico))
    for i in site:
        print("Pour le site: ",i[1])
        categorie=input("Dans quelle catégorie veux-tu la mettre ? :")
        while int(categorie) not in dico_c:
            print("La catégorie n'est pas valide")
            categorie=input("Dans quelle catégorie veux-tu la mettre ? :")
        dico_c[int(categorie)].add(i[0])
    return dico_c


def liste2(dico,dico_c):
    categorie=input("Quelle catégorie veux-tu avoir le page rank ? :")
    i=dico[categorie]
    tab=[]
    for j in dico_c[i]:
        tab.append(j)
    return tab



#dico2=cree_dict2()
#print("dico2",dico2)

#site=random_site("id-titre.txt",1)
#print(site)

#dico3=categorisation2(dico2,site)
#print("dico3",dico3)

#print(liste2(dico2,dico3))

"""col=liste2(dico2,dico3)
print(col)
row=np.ones(len(col))
print(row)"""
#y=sps.csr_matrix(([1]*len(row),(row,col)),shape=(1,100000000))
#print(y)

y=sps.csr_matrix([1],([1,1],[1000,12]),(100,1000))
print(y)
