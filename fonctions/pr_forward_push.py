import numpy as np

def pr_forward_push(dico,alpha,epsilon,perso,liste=[]):
    size=len(dico)

    #creation de y
    if perso:
        y=np.zeros(size)
        for i in liste:
            y[i]=1
        r=y*(1-alpha)/len(liste)

    else:
        r=np.array([(1-alpha)/size]*size)


    #calcul du page rank
    p=np.zeros(size)


    while max(r)>epsilon:
        u=np.argmax(r)
        x=r[u]
        p[u]+=x
        r[u]-=x

        voisins=dico[u]
        num_voisins=len(voisins)

        for i in voisins:
            r[i]+=alpha*x/num_voisins

    return p