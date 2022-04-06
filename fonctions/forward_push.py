import numpy as np

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