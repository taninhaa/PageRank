import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
import scipy
import seaborn


# Power iteration avec la somme
def power_iteration(dict1,tab,alpha): # fonction qui va calculer la valeur d'une page rank une par une
    nb_sommet=len(dict1)
    page_rank_final=np.zeros(nb_sommet) # tableau avec les nouvelles valeurs de page rank
    constante=(1-alpha)/nb_sommet

    for cles in dict1: # parcours de tous les sommets de notre graphe
        #print("cles",cles)
        somme=0
        for cles2 in dict1: # on parcours tous les sommets de notre graphe
            if cles in dict1[cles2]: # si un sommet de notre premier parcours se trouve dans l'ensemble on va l'ajouter avec la formule
                #print("sommet",cles2)
                somme=somme+(tab[cles2]/len(dict1[cles2]))  
                #print("valeur du page rank",tab[cles2-1])
                #print("nombre d'arcs sortants",len(dict1[cles2]))
        page_rank_final[cles]=alpha*somme+constante
    return page_rank_final

#Power iteration avec matrice
def creation_p(dict2): # conversion de notre dictionnaire à la matrice de transition
    nb_sommet=len(dict2)
    P=np.zeros((nb_sommet,nb_sommet))
    for cle in dict2:
        for sommet in dict2[cle]:
            P[cle,sommet]=1/len(dict2[cle])
    return P

def power_iteration_matrice(dict2,pi,alpha): # calcul de la valeur du page rank de manière matricielle
    nb_sommet=len(dict2)
    P=creation_p(dict2)
    constante=((1-alpha)/nb_sommet)*np.ones(nb_sommet)
    return alpha*np.dot(pi,P)+constante

#Power iteration avec sparse
def dict_sparse(dict2):
    data=[]
    row_ind=[]
    col_ind=[]
    for cle in dict2:
        for sommet in dict2[cle]:
            data.append(1/len(dict2[cle]))
            row_ind.append(cle)
            col_ind.append(sommet)
    return scipy.sparse.csr_matrix((data,(row_ind,col_ind)),shape=(len(dict2),len(dict2)))

def dict_sparse2(dict2):
    data=[]
    row_ind=[]
    col_ind=[]
    for cle in dict2:
        for sommet in dict2[cle]:
            row_ind.append(cle)
            col_ind.append(sommet)
    return row_ind,col_ind

