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
    data=np.loadtxt("aretes.txt")
    degre_sortant=data[:,0]
    id=[]
    tab=[]
    with open(site,'r') as f:
        lines=f.readlines()
        for i in range(n):
            x=random.randint(0,len(lines))
            while(x not in degre_sortant):
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

def creation_dict_titre(site):
    dict_final=dict()
    with open(site,'r') as f:
        lines=f.readlines()
        for i in range(len(lines)):
            tab=lines[i]
            res=''
            condition=0
            for j in tab:
                if(j=='\t'):
                    condition=1
                if(j!='\n'  and j!='\t' and condition==1):
                    res= res + j
            dict_final[res]=''
    return dict_final

def cree_dict_vide(size): # Cree un dictionnaire vide avec comme cle un entier qui represente la catégorie
    dico=dict()
    for i in range(size):  
        dico[i]=set()
    return dico

def categorisation_manuelle(dico,site): # fonction qui permet de catégoriser les sites de manière manuelle
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

def liste(dico,dico_c,categorie): # fonction qui te donne la liste des sites qui correspondent à la catégorie qu'on veut avec leur id
    """categorie=input("Quelle catégorie veux-tu avoir le page rank ? :")
    while categorie not in dico:
            print("La catégorie n'est pas valide")
            categorie=input("Quelle catégorie veux-tu avoir le page rank ? :")"""
    tab=[]
    for j in dico_c[categorie]:
        tab.append(j)
    return tab

"""def categorisation_automatique(n):
    rows,cols=reader_lists("aretes.txt")
    dico_entier,dico_final=cree_dict()
    site=random_site("id-titre.txt",n)
    dico_categorie=categorisation_manuelle(dico_entier,site)

    resultat=dict()
    for cle in dico_categorie:
        liste_perso=liste(dico_entier,dico_categorie,cle)
        pr=pr_power_iteration_sparse(rows,cols,0.85,1e-10,True,liste_perso)
        resultat[cle]=pr
    
    for i in range(len(pr)):
        categorie_max=0
        valeur_max=0
        for cle in resultat:
            if(resultat[cle][i]>valeur_max):
                valeur_max=resultat[cle][i]
                categorie_max=cle
        for cle2 in dico_entier:
            if categorie_max==dico_entier[cle2]:
                categorie_str=cle2
        dico_final[categorie_str].add(i)

        with open("categorie.txt","w") as f:
            for i in range (len(pr)):
                for cle in dico_final:
                    if i in dico_final[cle]:
                        f.write(("%d %s\n")%(i,cle))
    return dico_final

dico_final=categorisation_automatique(2)
for cle in dico_final:
    print(cle)
    print(dico_final[cle])
    input()"""