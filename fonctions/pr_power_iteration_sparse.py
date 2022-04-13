import numpy as np
import scipy.sparse as sps

def pr_power_iteration_sparse(rows,cols, alpha, epsilon,perso,liste=[]):
    size=max(max(rows),max(cols))+1
    A=sps.csr_matrix(([1]*len(rows),(rows,cols)),shape=(size,size))
    A=A+sps.eye(size)
    D=A.dot([1]*size)
    Dinv=sps.diags([np.reciprocal(D)],[0])
    P=Dinv.dot(A)
    
    #creation de y  
    if perso:
        y=[0]*size
        for i in liste:
            y[i]=1
        pi=np.array(y)
        y=np.array(y)
        y=(1-alpha)*y/len(liste) 
        pi_avant=[0]*size 
    else:
        y=np.array([(1-alpha)/size]*size)
        pi=[0]*size
        pi_avant=np.array(y)

    #Calcul du P transpose
    Pt=P.transpose()

    #Calcul du page rank
    while(np.linalg.norm(pi-pi_avant)>epsilon):
        pi_avant=pi
        pi=alpha*(Pt.dot(pi_avant))+y
    
    return pi