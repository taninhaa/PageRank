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

#Fonction qui calcule la page rank avec la formule de la somme
def power_iteration_somme(dict1,alpha,epsilon):
    nb_sommet=len(dict1)
    constante=(1-alpha)/nb_sommet
    x0=np.zeros(nb_sommet)
    x1=np.ones(nb_sommet)
    while(np.linalg.norm(x1-x0)>epsilon): 
        x0=np.copy(x1)
        for cles in dict1: 
            somme=0
            for cles2 in dict1: 
                if cles in dict1[cles2]:
                    somme=somme+(x0[cles2]/len(dict1[cles2]))
            x1[cles]=alpha*somme+constante
    return x1

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
	e = [1/size]*size
	M = sps.eye(size) - alpha*P
	pr_exact = spl.spsolve(M, e)
	return pr_exact
	
#Forward push avec dictionnaire en entrée
def forward_push(dico, alpha, epsilon):
	size = len(dico)
	r = np.array([(1-alpha)/size]*size)
	p = np.zeros(size)
	counter = 0
	while max( r ) > epsilon : 
		u = np.argmax( r )
		x = r[u]
		p[u] += x
		r[u] -= x
		
		voisins = dico[u]
		num_voisins = len(voisins)
		for i in voisins:
			r[i] += alpha*x/num_voisins		
		counter += 1
	return p

#Forward push avec dictionnaire en entrée page rank perso
def forward_push_perso(dico, alpha, epsilon,liste):
	size = len(dico)
	#creation y
	y=np.zeros(size)
	for i in liste:
		y[i]=1
	r = y*(1-alpha)/len(liste) # ici r c'est y*(1-alpha)
	p = np.zeros(size)
	counter = 0
	while max( r ) > epsilon : 
		u = np.argmax( r )
		x = r[u]
		p[u] += x
		r[u] -= x
		
		voisins = dico[u]
		num_voisins = len(voisins)
		for i in voisins:
			r[i] += alpha*x/num_voisins		
		counter += 1
	return p

#Fonction qui calcule la page rank perso avec somme
def power_iteration_somme_perso(dict1,alpha,epsilon,liste):
    nb_sommet=len(dict1)

    #creation y
    y=np.zeros(nb_sommet)
    for i in liste:
        y[i]=1
    x1=y/len(liste)
    y=(1-alpha)*y/len(liste)
    x0=np.zeros(nb_sommet)
    while(np.linalg.norm(x1-x0)>epsilon): 
        x0=np.copy(x1)
        for cles in dict1: 
            somme=0
            for cles2 in dict1: 
                if cles in dict1[cles2]:
                    somme=somme+(x0[cles2]/len(dict1[cles2]))
            x1[cles]=(alpha*somme)+y[cles]
    return x1

#Fonction qui calcule la page rank perso de manière matricielle
def pagerank_sparse_perso(rows, cols, alpha, epsilon,liste):
	size = max(max(rows), max(cols)) + 1
	A = sps.csr_matrix(([1]*len(rows), (rows, cols)), shape=(size,size))
	A = A + sps.eye(size)
	D = A.dot([1]*size)
	Dinv = sps.diags([np.reciprocal(D)], [0])
	P = Dinv.dot(A)

	#creation de y
	y=np.zeros(size)
	for i in liste:
		y[i]=1
	pi=np.array(y)
	y=(1-alpha)*y/len(liste)
	pi_avant=[0]*size
	Pt=P.transpose()
	iteration=0
	while(np.linalg.norm(pi-pi_avant)>epsilon):
		pi_avant=pi
		pi=alpha*(Pt.dot(pi_avant))+y
		iteration=iteration+1
	return pi,iteration