import csv
import numpy as np

def tri(lignes):
    pagerank=[]     
    with open("pagerank.txt", newline='') as csvfile:
        for row in csv.reader(csvfile, delimiter=' ', quotechar='|'): 
            for i in range(0,len(lignes)):
                if int(lignes[i])==row[0]:
                #print(lignes[i])
                    pagerank.append(int(row[1])) 
        return pagerank

L="1 845 850 851 1379 1816 13388 23537 33805 35018 52417 54494 63426 63427 63438 63439 63440 63441 63442 63443 63444 63448"
L1=L.split(' ')
#print(L1)
pagerank1=tri(L1)
print(pagerank1)

    
            
                