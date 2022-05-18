import csv
import random
from re import X
from time import time
import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi
from fonctions.creation_dict import dico_construction
import scipy.sparse as sps
import scipy.sparse.linalg as spl
import seaborn
import sys
import time
sys.path.append("./fonctions")
from read_file_into_row_col import reader_lists

def comparaison_erreur_power(rows,cols,gamma,alpha):
    size=max(max(rows),max(cols))+1
    A=sps.csr_matrix(([1]*len(rows),(rows,cols)),shape=(size,size))
    A=A+sps.eye(size)
    D=A.dot([1]*size)
    Dinv=sps.diags([np.reciprocal(D)],[0])
    P=Dinv.dot(A)

    y=np.array([(1-alpha)/size]*size)
    pi=[0]*size
    pi_avant=np.array(y)

    #Valeur exacte
    e=np.ones(size)
    A=np.transpose((np.identity(size)-alpha*P))
    B=((1-alpha)/size)*np.transpose(e)
    pi_exacte=np.linalg.solve(A,B)
    #print("valeur exacte",pi_exacte)
    #Calcul du P transpose
    Pt=P.transpose()

    #Calcul du page rank
    t1=time.time()
    while(np.linalg.norm(pi_exacte-pi>gamma)):
        pi_avant=pi
        pi=alpha*(Pt.dot(pi_avant))+y
    t2=time.time()
    return t2-t1

def comparaison_erreur_push(rows,cols,gamma,alpha):
    size=max(max(rows),max(cols))+1
    A=sps.csr_matrix(([1]*len(rows),(rows,cols)),shape=(size,size))
    A=A+sps.eye(size)
    D=A.dot([1]*size)
    Dinv=sps.diags([np.reciprocal(D)],[0])
    P=Dinv.dot(A)

    #Valeur exacte
    e=np.ones(size)
    A=np.transpose((np.identity(size)-alpha*P))
    B=((1-alpha)/size)*np.transpose(e)
    pi_exacte=np.linalg.solve(A,B)

    dico=dico_construction(rows,cols)
    r = np.array([(1-alpha)/size]*size)
    p = np.zeros(size)
    t1=time.time()
    while(np.linalg.norm(pi_exacte-p>gamma)):
        u=np.argmax(r)
        x=r[u]
        p[u]+=x
        r[u]-=x

        voisins=dico[u]
        num_voisins=len(voisins)
        for i in voisins:
            r[i]+=alpha*x/num_voisins
    t2=time.time()
    return t2-t1

rows,cols=reader_lists("arete_4000.txt")

erreur_power=np.zeros(10)
erreur_push=np.zeros(10)
alpha=np.arange(0,1,0.1)
print(alpha)
mean_power = np.zeros(100)
mean_push=np.zeros(100)
for i in range(len(alpha)):
    for j in range(10):
        mean_power[j] = comparaison_erreur_power(rows,cols,1e-3,alpha[i])
        mean_push[j] = comparaison_erreur_push(rows,cols,1e-3,alpha[i])
    erreur_power[i] = mean_power.mean()
    erreur_push[i] = mean_push.mean()
    print("power",erreur_power[i])
    print("push",erreur_push[i])

plt.plot(alpha,erreur_power,label= "Power Iterative")
plt.plot(alpha,erreur_push,label= "Forward Push")
plt.xlabel("alpha")
plt.ylabel("temps en seconde")
plt.yscale("log")
plt.title("Vitesse de convergence en fonction des valeurs d'alpha")
plt.legend(loc="best")
plt.show()