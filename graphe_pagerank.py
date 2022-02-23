import wikipediaapi

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


wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Python_(programming_language)')
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
print("Page - Exists: %s" %     page_missing.exists())
# Page - Exists: False

