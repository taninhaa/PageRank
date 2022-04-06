#!/bin/bash
#YOoo c'est le script de Tania et Bastien !!
# Pour compiler chmod 755 nomfichier

#Test
echo Hello les copains

#Retourne les ID en lien avec le mot recherché
ID=$(grep "\\b$1\\b" id-titre.txt | awk -F'\t' '{print $1}')
echo $ID

#Retourne une liste avec (id1,valueid1,id2,valueid2, ...)
IDPagerank=()
for id in $ID
do
    IDPagerank+=($(grep "^$id\\b" pagerank.txt))
done



#print test

for i in ${!IDPagerank[@]}
do  
    echo ${IDPagerank[$i]}
done

exit 0

# commande1 | commande2 qui utilise le res1
# awk lis un res par ligne et colonne comme un tableau
#Titres = $()
#echo $Titres
#python3 fichier_list.py $1;