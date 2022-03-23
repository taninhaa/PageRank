from numpy import Infinity
import wikipediaapi
from tqdm import tqdm
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

from fichier_graphe import conversion_dict_fichier

def scraping(titre):
	wiki_wiki = wikipediaapi.Wikipedia('en')
	# Dictionnaire d'identifients
	dico_nom_id, dico_id_nom = dict(), dict()
	page_debut = titre
	dico_nom_id[page_debut] = 0
	dico_id_nom[0] = page_debut
	
	with open("titres.txt", "w") as file:
		file.write("%d\t%s\n"%(0,page_debut))

	# Queue pour parcourir le graphe
	liste_pages = deque([dico_nom_id[page_debut]])  #Création d'une liste d'identifiants 
	visited = {dico_nom_id[page_debut]} #ensemble de page visitées 

	# Graphe 
	graphe = dict()

	compteur = 0
	while compteur < 100000:
		print(compteur)
		#print('longeur de liste_pages ', len(liste_pages)) 
		compteur += 1
		page_id = liste_pages.popleft() #Enleve le premier identifiant de la liste 
		page_obj = wiki_wiki.page( dico_id_nom[page_id] ) #Cherche les voisins de l'identifiant précédent

		if page_id not in graphe: graphe[page_id] = set() #Si l'identifiant n'est pas dans le graphe, on l'ajoute 

		for p in page_obj.links: 
			#On cherche tous les voisions de la page identifiant

			if p not in dico_nom_id: 
				#Si le voisin n'est pas dans le dictionnaire, on l'ajoute 
				new_id = len(dico_nom_id)  #On l'identifie 
				dico_nom_id[p] = new_id 
				dico_id_nom[new_id] = p
				with open("titres.txt", "a") as file:
					file.write("%d\t%s\n"%(new_id,p))
		
			graphe[page_id].add( dico_nom_id[p] ) #On ajoute tous les voisins de l'identifiant dans le graphe
			
			if dico_nom_id[p] not in visited: 
				#On indique qu'on le visite 
				liste_pages.append( dico_nom_id[p] )
				visited.add( dico_nom_id[p] )
				
	return (graphe,len(dico_nom_id))

	"""	
	for noeud in graphe:
		print('noeud : ', noeud)
		print('voisins : ', graphe[noeud])
		input('--')
	"""

graphe1, taille=scraping('Python_(programming_language)')

conversion_dict_fichier("arete_graphe.txt", graphe1)