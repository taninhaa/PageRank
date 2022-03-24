from audioop import add
import csv
import numpy as np

def reader_lists(fileName):
	with open(fileName, 'r') as csvfile:
		rows = []
		cols = []
		edgelist = csv.reader(csvfile, delimiter=' ')
		for line in edgelist:
			rows.append( int(line[0]) )
			cols.append( int(line[1]) )

		return rows, cols

def cree_dict(rows,cols):
    size=len(rows)
    dico=dict()
    for i in range(size):
        if rows[i] not in dico: dico[rows[i]]=set([rows[i]])
        if cols[i] not in dico: dico[cols[i]]=set([cols[i]])
        dico[rows[i]].add(cols[i])
    return dico

def exact(rows,cols,alpha):
    size = max(max(rows), max(cols)) + 1 #size=N
    A = sps.csr_matrix(([1]*len(rows), (rows, cols)), shape=(size,size))
    A = A + sps.eye(size)
    D = A.dot([1]*size)
    Dinv = sps.diags([np.reciprocal(D)], [0])
    P = Dinv.dot(A).transpose()
    e=[1]*size
    M=sps.eye










def forward_push(dico,alpha,epsilon):
    size=len(dico)
    r=np.array([(1-alpha)/size]*size)
    p=np.zeros(size)
    iteration=0
    while(np.max(r)>epsilon):#norme infinie
        if iteration%100==O: print(iteration)
        u=np.argmax(r)
        x=r[u]
        p[u]=p[u]+x
        r[u]=r[u]-x

        voisins=dico[u]
        num_voisins=len(voisins)
        for i in voisins:
            r[i]+=alpha*x/num_voisins
        iteration+=1


    return p


    

