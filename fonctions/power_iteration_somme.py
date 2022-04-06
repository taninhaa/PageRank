import numpy as np

# Calcul du page rank avec la somme
def power_iteration_somme(dict1,alpha,epsilon):
    nb_sommet=len(dict1)
    constante=(1-alpha)/nb_sommet
    x0=np.zeros(nb_sommet)
    x1=np.ones(nb_sommet)
    while(np.linalg.norm(x1-x0)>epsilon): 
        x0=np.copy(x1)
        for cles in dict1: 
            somme=0
            for cles2 in dict1: 
                if cles in dict1[cles2]:
                    somme=somme+(x0[cles2]/len(dict1[cles2]))
            x1[cles]=alpha*somme+constante
    return x1