import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
import scipy.sparse as sps
import scipy.sparse.linalg as spl
import seaborn
import csv

#Fonction qui va lire un fichier et qui donne deux tableaux avec les lignes et les colonnes
def reader_lists(fileName):
	with open(fileName, 'r') as csvfile:
		rows = []
		cols = []
		edgelist = csv.reader(csvfile, delimiter=' ')
		for line in edgelist:
			rows.append( int(line[0]) )
			cols.append( int(line[1]) )
		return rows, cols

#Fonction qui va convertir les deux tableaux lignes , colonnes et qui donne le dictionnaire
def dico_construction(rows,cols):
	size = len(rows)
	dico = dict()
	for i in range(size):
		if rows[i] not in dico: dico[rows[i]] = set([rows[i]])	
		if cols[i] not in dico: dico[cols[i]] = set([cols[i]])
		dico[rows[i]].add( cols[i] )
	return dico

#Fonction qui convertit un dictionnaire en matrice de transition
def creation_p(dict2): 
    nb_sommet=len(dict2)
    P=np.zeros((nb_sommet,nb_sommet))
    for cle in dict2:
        for sommet in dict2[cle]:
            P[cle,sommet]=1/len(dict2[cle])
    return P


#Fonction qui calcule la valeur du page rank de manière matricielle en prenant en argument un dictionnaire
def power_iteration(dict2,alpha,epsilon):
    nb_sommet=len(dict2)
    P=creation_p(dict2)
    e=np.array([(1-alpha)/nb_sommet]*nb_sommet)
    pi_avant=np.array(e)
    pi=[0]*nb_sommet
    while(np.linalg.norm(pi-pi_avant)>epsilon):
        pi_avant=pi
        pi=alpha*np.dot(pi_avant,P)+e
    return pi

#Fonction qui calcule la valeur du page rank sans utiliser le dictionnaire avec sparse
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

#Fonction qui calcule la valeur exacte du page rank en prenant en entrée tableau de lignes et de colonnes 
def exact_pr(rows, cols, alpha):
	size = max(max(rows), max(cols)) + 1
	A = sps.csr_matrix(([1]*len(rows), (rows, cols)), shape=(size,size))
	A = A + sps.eye(size)
	D = A.dot([1]*size)
	Dinv = sps.diags([np.reciprocal(D)], [0])
	P = Dinv.dot( A ).transpose()
	e = [1]*size
	M = sps.eye(size) - alpha*P
	pr_exact = spl.spsolve(M, e)
	return pr_exact

#Forward push avec dictionnaire en entrée
def forward_push(dico, alpha, epsilon, pr_exact):
	size = len(dico)
	r = np.array([(1-alpha)]*size)
	p = np.zeros(size)
	counter = 0
	while max( r ) > epsilon : 
		u = np.argmax( r )
		x = r[u]
		if counter % 100 == 0: print(counter, np.linalg.norm(pr_exact - p))
		p[u] += x
		r[u] -= x
		
		voisins = dico[u]
		num_voisins = len(voisins)
		for i in voisins:
			r[i] += alpha*x/num_voisins		
		counter += 1
	return p

