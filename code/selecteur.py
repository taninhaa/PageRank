import wikipediaapi
import sys


wiki = wikipediaapi.Wikipedia('en')

sujet = ""
for i in range(2,len(sys.argv)):
    if i==2:
        sujet += sys.argv[i]
    else:
        sujet += " " + sys.argv[i]
    

pagewiki = wiki.page(sujet)

if pagewiki.exists():
    print("%s" % pagewiki.summary[0:1000])
else:
    print(sujet)
    print("Erreur : Page introuvable")