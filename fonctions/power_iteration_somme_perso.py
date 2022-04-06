import numpy as np

#Fonction qui calcule la page rank perso avec somme
def power_iteration_somme_perso(dict1,alpha,epsilon,liste):
    nb_sommet=len(dict1)

    #creation y
    y=np.zeros(nb_sommet)
    for i in liste:
        y[i]=1
    x1=y/len(liste)
    y=(1-alpha)*y/len(liste)
    x0=np.zeros(nb_sommet)
    while(np.linalg.norm(x1-x0)>epsilon): 
        x0=np.copy(x1)
        for cles in dict1: 
            somme=0
            for cles2 in dict1: 
                if cles in dict1[cles2]:
                    somme=somme+(x0[cles2]/len(dict1[cles2]))
            x1[cles]=(alpha*somme)+y[cles]
    return x1