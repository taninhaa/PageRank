import numpy as np
import scipy.sparse as sps

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