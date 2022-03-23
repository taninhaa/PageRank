import csv
import time

def conversion_list_fichier_graphe(fichier):
    ligne =[]
    colonne = []
    with open(fichier, newline='') as csvfile:
        spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            ligne.append(int(row[0]))
            colonne.append(int(row[1]))

    return ligne,colonne

t1 = time.time()
(ligne,colonne) = conversion_list_fichier_graphe("soc-buzznet.mtx")
t2 = time.time()
print(t2-t1)
for i in range(5):
    print(ligne[i],colonne[i])
