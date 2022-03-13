import csv 

""" Fonction qui permet de lire un fichier d'aretes et de créer le dictionnaire correspondant"""
#Graphe
graphe1={}

with open('bio-CE-CX.edges', newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        a=int(row[0])
        b=int(row[1])
        if a not in graphe1:
            graphe1[a]= set()
        if b not in graphe1[a]:
            graphe1[a].add(b)
            
#Affiche le graphe
for i in graphe1.items():
    print(i) 
