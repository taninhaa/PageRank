import numpy as np

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