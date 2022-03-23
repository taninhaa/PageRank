import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
import scipy.sparse as sps
import seaborn
import csv


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
                somme=somme+(tab[cles2]/len(dict1[cles2]))  
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
def dict_sparse(dict2): # retourne la matrice sparse
    data=[]
    row_ind=[]
    col_ind=[]
    for cle in dict2:
        for sommet in dict2[cle]:
            data.append(1/len(dict2[cle]))
            row_ind.append(cle)
            col_ind.append(sommet)
    return sps.csr_matrix((data,(row_ind,col_ind)),shape=(len(dict2),len(dict2)))

def power_iteration_sparse(dict2,pi,alpha):
    nb_sommet=len(dict2)
    P=dict_sparse(dict2)
    constante=((1-alpha)/nb_sommet)*np.ones(nb_sommet)
    P_t=P.transpose()
    pi_t=pi.transpose()
    return (alpha*P_t.dot(pi_t)).transpose()+constante

def power_iteration_sparse_erreur(dict2,pi,alpha,epsilon): # avec erreur
    nb_sommet=len(dict2)
    P=dict_sparse(dict2)
    constante=((1-alpha)/nb_sommet)*np.ones(nb_sommet)
    P_t=P.transpose()
    page_rank=np.zeros((1,len(dict2)))
    iteration=0
    while(np.linalg.norm(page_rank-pi)>epsilon):
        iteration=iteration+1
        page_rank=pi
        pi=(alpha*P_t.dot(page_rank.transpose())).transpose()+constante
    return pi,iteration

def dict_sparse2(dict2): # retourne les indices de lignes et de colonnes des éléments non nuls
    data=[]
    row_ind=[]
    col_ind=[]
    for cle in dict2:
        for sommet in dict2[cle]:
            row_ind.append(cle)
            col_ind.append(sommet)
    return row_ind,col_ind

def pagerank_sparse(rows, cols, alpha, epsilon):	
	size = max(max(rows), max(cols)) + 1
	A = sps.csr_matrix(([1]*len(rows), (rows, cols)), shape=(size,size))
	A = A + sps.eye(size)
	D = A.dot([1]*size)
	Dinv = sps.diags([np.reciprocal(D)], [0])
	P = Dinv.dot(A)

	pi=np.ones((1,max(max(rows), max(cols)) + 1))/(max(max(rows), max(cols)) + 1)
	constante=(1-alpha)/size*np.ones(size)
	P_t=P.transpose()
	pi_t=pi.transpose()
	page_rank=alpha*P_t.dot(pi_t).transpose()+constante
	page_rank_t=page_rank.transpose()
	print(page_rank_t)
	while(np.linalg.norm(page_rank_t-pi_t)>epsilon):
		pi_t=page_rank_t
		page_rank_t=alpha*P_t.dot(pi_t)+constante
	return page_rank
