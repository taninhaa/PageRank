class sommet():
    def __init__(self,label,value=0):
        self.label=label
        self.value=value

class arete():
    def __init__(self,sommet1,sommet2):
        self.sommet1=sommet1
        self.sommet2=sommet2

class graph():
    def __init__(self,nb_arete,nb_sommet,liste_sommet_adjacent):
        self.nb_arete=nb_arete
        self.nb_sommet=nb_sommet
        self.dict_address={sommet:liste_sommet_adjacent}



"""
def power_iteration(graphique):
    for sommet in graphique.dict_address:

        dict[sommet]"""

