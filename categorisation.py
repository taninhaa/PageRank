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

def cree_dict(): #Cree un dicionnaire qui associe chaque catégorie à un entier
    size=input("Nombre de catégorie ? :")
    len=int(size)
    dico=dict()
    for i in range(len):
        categorie=input("Nom de la catégorie ? :")
        dico[categorie]=i
    dico["Autres"]=len
    return dico

def random_site(site,n): # Cree un tuple de n sites aléatoires avec l'id et le titre
    id=[]
    tab=[]
    with open(site,'r') as f:
        lines=f.readlines()
        for i in range(n):
            x=random.randint(0,2000)
            #x=random.randint(0,len(lines))
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

def cree_dict_vide(size): # Cree un dictionnaire vide avec comme cle un entier qui represente la catégorie
    dico=dict()
    for i in range(size):  
        dico[i]=set()
    return dico

def categorisation(dico,site): # fonction qui permet de catégoriser les sites
    print("Les différentes catégories sont")
    print(dico)
    print("Rentrez l'entier associé")
    dico_c=cree_dict_vide(len(dico))
    for i in site:
        print("Pour le site: ",i[1])
        categorie=input("Dans quelle catégorie veux-tu la mettre ? :")
        while int(categorie) not in dico_c:
            print("La catégorie n'est pas valide")
            categorie=input("Dans quelle catégorie veux-tu la mettre ? :")
        dico_c[int(categorie)].add(i[0])
    return dico_c

def liste(dico,dico_c): # fonction qui te donne la liste des sites qui correspondent à la catégorie qu'on veut avec leur id
    categorie=input("Quelle catégorie veux-tu avoir le page rank ? :")
    while categorie not in dico:
            print("La catégorie n'est pas valide")
            categorie=input("Quelle catégorie veux-tu avoir le page rank ? :")
    i=dico[categorie]
    tab=[]
    for j in dico_c[i]:
        tab.append(j)
    return tab

rows,cols=reader_lists("aretes.txt")

dico2=cree_dict()

site=random_site("id-titre.txt",20)
print(site)

dico3=categorisation(dico2,site)
liste2=liste(dico2,dico3)
print(liste2)
pr=pr_power_iteration_sparse(rows,cols,0.85,1e-10,True,liste2)
for i in range(len(pr)):
    if(pr[i]>0):
        input()
        print(pr[i])

