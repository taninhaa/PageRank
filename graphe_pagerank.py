import wikipediaapi
import numpy as np

class sommet():
    def __init__(self,label,value=0):
        self.label = label
        self.value = value

class arete():
    def __init__(self,sommet1,sommet2):
        self.sommet1 = sommet1
        self.sommet2 = sommet2

class graphe():
    def __init__(self,sommet,liste_sommet_adjacent =()):
        self.nb_arete = 0
        self.nb_sommet = 1
        # orienté
        self.dict_successeur = {sommet:liste_sommet_adjacent}

    def ajoute_sommet(self,sommet,liste_sommet_adjacent):
        if sommet not in self.dict_adjacent:
            self.dict_adjacent[sommet] = liste_sommet_adjacent
        else:
            for sommet_adjacent in liste_sommet_adjacent:
                if sommet_adjacent not in self.dict_adjacent:
                    self.dict_adjacent[sommet] += (sommet_adjacent)

    def ajoute_arete(self,liste_arete):
        for arete in liste_arete:
            if arete.sommet1 in self.dict_adjacent:
                if arete.sommet2 not in self.dict_adjacent[arete.sommet1]:
                    self.dict_adjacent[arete.sommet1] += (arete.sommet2)

"""
wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Python_(programming_language)')
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
print("Page - Exists: %s" %     page_missing.exists())
# Page - Exists: False """

"""N=5
dict1={1:{2,3}, 2:{3,5}, 3:{4}, 4:{2}, 5:{4}}
valeur_page_rank=[]
print( "longueur ",len(dict1[1]))
for i in range(N):
    valeur_page_rank[i]=1/N
print(valeur_page_rank)
for cle,valeur in dict1.items():
    print(cle)
    print(valeur)
#print(dict1)
alpha=0.85
tab=np.ones(N)/N
#print(tab)"""

def power_iteration(dict1,tab,N,alpha):
    page_rank_final=np.zeros(N)
    page_rank=tab
    constante=(1-alpha)/N

    for cles in dict1:
        print("cles",cles)
        somme=0
        for cles2 in dict1:
            if cles in dict1[cles2]:
                print("yes")
                print("sommet",cles2)
                somme=somme+(tab[cles2-1]/len(dict1[cles2]))
                print("valeur du page rank",tab[cles2-1])
                print("nombre d'arcs sortants",len(dict1[cles2]))
        page_rank_final[cles-1]=alpha*somme+constante
    return page_rank_final

N2=3
dict2={1:{2,3}, 2:{3}, 3:{1}}
tab2=np.ones(N2)/N2
for i in range(10):
    tab2=power_iteration(dict2,tab2,N2,0.85)
    print(tab2)


