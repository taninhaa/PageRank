import csv

#Fonction qui va lire un fichier et qui donne deux tableaux avec les lignes et les colonnes
def reader_lists(fileName):
	with open(fileName, 'r') as csvfile:
		rows = []
		cols = []
		edgelist = csv.reader(csvfile, delimiter='\t')
		for line in edgelist:
			rows.append( int(line[0]) )
			cols.append( int(line[1]) )
		return rows, cols