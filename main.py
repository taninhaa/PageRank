import wikipediaapi
from tqdm import tqdm
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

wiki_wiki = wikipediaapi.Wikipedia('en')

# Dictionnaire d'identifients
dico_nom_id, dico_id_nom = dict(), dict()
page_debut = 'Python_(programming_language)'
dico_nom_id[page_debut] = 0
dico_id_nom[0] = page_debut

# Queue pour parcourir le graphe
liste_pages = deque([dico_nom_id[page_debut]])
visited = {dico_nom_id[page_debut]}

# Graphe 
graphe = dict()

compteur = 0
while compteur < 10:
	print('longeur de liste_pages ', len(liste_pages)) 
	compteur += 1
	page_id = liste_pages.popleft()
	page_obj = wiki_wiki.page( dico_id_nom[page_id] )

	if page_id not in graphe: graphe[page_id] = set()

	for p in page_obj.links: 
		
		if p not in dico_nom_id: 
			new_id = len(dico_nom_id)
			dico_nom_id[p] = new_id 
			dico_id_nom[new_id] = p
	
		graphe[page_id].add( dico_nom_id[p] )
		
		if dico_nom_id[p] not in visited: 
			liste_pages.append( dico_nom_id[p] )
			visited.add( dico_nom_id[p] )
	
for noeud in graphe:
	print('noeud : ', noeud)
	print('voisins : ', graphe[noeud])
	input('--')
