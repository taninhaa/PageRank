import numpy as np

#Fonction qui convertit un dictionnaire en matrice de transition
def creation_p(dict2): 
    nb_sommet=len(dict2)
    P=np.zeros((nb_sommet,nb_sommet))
    for cle in dict2:
        for sommet in dict2[cle]:
            P[cle,sommet]=1/len(dict2[cle])
    return P