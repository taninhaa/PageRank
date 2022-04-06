import scipy.sparse as sps
import numpy as np

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