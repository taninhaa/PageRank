#Fonction qui va convertir les deux tableaux lignes , colonnes et qui donne le dictionnaire en ajoutant le self-loop
def dico_construction(rows,cols):
	size = len(rows)
	dico = dict()
	for i in range(size):
		if rows[i] not in dico: dico[rows[i]] = set([rows[i]])	
		if cols[i] not in dico: dico[cols[i]] = set([cols[i]])
		dico[rows[i]].add( cols[i] )
	return dico
