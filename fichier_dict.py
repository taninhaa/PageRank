import csv 

""" Fonction qui permet de lire un fichier d'aretes et de créer le dictionnaire correspondant"""
#Graphe
def conversion_dict_fichier_graphe(fichier):
    graphe={}

    with open(fichier, newline='') as csvfile:
        spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            a=int(row[0])
            b=int(row[1])
            if a not in graphe:
                graphe[a]= set()
            if b not in graphe[a]:
                graphe[a].add(b)
    return graphe
                
#Affiche le graphe
graphe1=conversion_dict_fichier_graphe('bio-CE-CX.edges')
for i in graphe1.items():
    print(i) 