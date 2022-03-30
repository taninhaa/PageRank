import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
import scipy.sparse as sps
import seaborn
import csv

def power_iteration_matrice_erreur(dict2,pi,alpha,epsilon): # calcul de la valeur du page rank de manière matricielle avec erreur epsilon
    nb_sommet=len(dict2)
    P=creation_p(dict2)
    e=np.array([(1-alpha)/nb_sommet]*nb_sommet)
    pi_avant=np.array(e)
    pi=[0]*nb_sommet
    while(np.linalg.norm(pi-pi_avant)>epsilon):
        pi_avant=pi
        pi=alpha*np.dot(pi_avant,P)+e
    return pi

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

	e=np.array([(1-alpha)/size]*size)
	pi_avant=np.array(e)
	pi=[0]*size
	Pt=P.transpose()

	while(np.linalg.norm(pi-pi_avant)>epsilon):
		pi_avant=pi
		pi=alpha*(Pt.dot(pi_avant))+e
	return pi
