import numpy as np

def pr_power_iteration_somme(dico,alpha,epsilon,perso,liste=[]):
    nb_sommet=len(dico)
    if perso:
        y=np.zeros(nb_sommet)
        for i in liste:
            y[i]=1
        x1=y/len(liste)
        y=(1-alpha)*y/len(liste)
    else:
        y=(np.ones(nb_sommet))*(1-alpha)/nb_sommet
        x1=np.ones(nb_sommet)
    x0=np.zeros(nb_sommet)
    iteration=0
    while(np.linalg.norm(x1-x0)>epsilon):
        x0=np.copy(x1)
        for cles in dico:
            somme=0
            for cles2 in dico:
                if cles in dico[cles2]:
                    somme=somme+(x0[cles2]/len(dico[cles2]))
            x1[cles]=(alpha*somme)+y[cles]
    return x1