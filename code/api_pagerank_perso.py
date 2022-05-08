import sys
from graphe_pagerank import reader_lists,pagerank_sparse_perso

#On recupère les ID
liste_ID = []
for ID in sys.argv[1:]: #sys.argv[0] == './code/api_pagerank_perso.py'
    liste_ID.append(int(ID))

#On recupère l'ensemble des arêtes sous forme matricielle
rows,cols = reader_lists("./data/aretes.txt")
alpha = 0.85
eps = 1e-10
#Calcule du pagerank personnalisé qui prend en compte les ID personnalisés
pi,iter = pagerank_sparse_perso(rows,cols,alpha,eps,liste_ID)


n_res = 0
#On renvoie les 5 meilleurs ID dans le script 
for ID in (-pi).argsort():
    if n_res == 5:
        break
    elif pi[ID] != 0:
        #On s'assure que le pagerank n'est pas nul
        n_res += 1
        print(ID)
        

