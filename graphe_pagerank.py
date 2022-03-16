
import wikipediaapi
import time 



#Pour la lecture: 
    #contents = f.readlines()
    #for line in contents:
    #   [arete1,arete2] = line.split('\t')


class sommet():
    def __init__(self,label,value=0):
        self.label = label
        self.id = 0
        self.value = value

class arete():
    def __init__(self,sommet1,sommet2):
        self.sommet1 = sommet1
        self.sommet2 = sommet2

class graphe():
    def __init__(self):
        self.nb_arete = 0
        self.nb_sommet = 0
        # orienté
        self.dict_successeur = {}
        """
        self.dict_predecesseur = {}
        for s_adjacent in liste_sommet_adjacent:#pas de doublon
            self.nb_arete += 1
            self.nb_sommet += 1
            self.dict_predecesseur[s_adjacent] = (sommet)
        """


    def ajoute_sommet(self,sommet,liste_sommet_adjacent):
        #Fonction qui ajoute un sommet avec sa liste d'adjacence dans un dictionnaire 
        if sommet not in self.dict_successeur:
            #Ajout du sommet dans le dictionnaire
            self.dict_successeur[sommet] = liste_sommet_adjacent #On ajoute la liste de sommet 
            self.nb_sommet += 1 #Un sommet de +

        else:
            #Cas ou le sommet ets deja présent dans le graphe 
            for sommet_adjacent in liste_sommet_adjacent:
                #Pour les sommets de la liste d'adjacence 
                if sommet_adjacent not in self.dict_successeur[sommet]:
                    #Si le sommet adjacent n'est pas dans la liste d'adjacence du dictionnaire, 
                    # on l'ajoute à l'ensemble de sommets adjacents 
                    self.dict_successeur[sommet] += (sommet_adjacent)

        self.nb_arete += len(liste_sommet_adjacent) #ajout du nombre d'arete supplementaire 

c=graphe()
c.ajoute_sommet(2,{})


"""def print_links(page):
    #Acces aux hyperliens de la page 
        links = page.links
        for title in sorted(links.keys()):
            print("%s: %s" % (title, links[title]))
"""
start3=time.time()
def found_id (title):
    #Fonction qui permet d'associer le titre d'une page à des numéros
    id = 1
    with open('id_wiki.txt','r') as f:
        contents = f.readlines() #On importe les lignes 
        for line in contents:
            #Pour chaque lignes on regarde si le titre est dans la ligne 
            if title==line:
                return id #On retourne le numéro correspondant
            id +=1
        
    # si il n'existe pas on le créé
    with open('id_wiki.txt','a') as f:
        f.write('%s\n'%title)
        return id 
end3=time.time()

print("found id",end3-start3)

start=time.time()

def scrapping(sujet,wiki):
    #Fonction qui permet de mettre d'afficher dans un fichier la correspondance
    #  entre le titre et le numéro du graphe
    pagewiki = wiki.page(sujet)
    #On cherche la page sur wikipedia 
    if pagewiki.exists():
        #si elle est existe, on lui attribut un identifiant
        id_sujet = found_id(sujet)
        with open('wiki.txt','a') as f:
            #print(len(pagewiki.links.keys()))
            for title in pagewiki.links.keys():
                
                f.write('%d\t%d\n'%(id_sujet,found_id(title)))
end=time.time()

print("scrapping time: ", end-start)

#root = graphe()
wiki = wikipediaapi.Wikipedia('en')# titre : 18.6 caratères en moyenne sur la page 'Python_(programming_language)'
#graphe_scrapping('Python_(programming_language)',wiki,root)
#print_text(root) 
scrapping('Python_(programming_language)',wiki)

start1=time.time()

with open('id_wiki.txt','r') as f:
    contents = f.readlines()
    for line in list(contents)[1:]:
        print(str(line[:-2]))
        scrapping(line[:-2],wiki)

end1=time.time()
print("lecture fichier id_wiki", end1-start1)