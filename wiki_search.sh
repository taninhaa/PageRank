#!/bin/bash
#YOoo c'est le script de Tania et Bastien !!
# Pour compiler chmod 755 nomfichier

ChercheID(){
    #Retourne les ID en lien avec le mot recherché
    ID=$(grep "\\b$1\\b" id-titre.txt | awk -F'\t' '{print $1}')

    #Retourne une liste avec (id1,valueid1,id2,valueid2, ...)
    IDPagerank=()
    for id in $ID
    do
        IDPagerank+=($(grep "^$id\\b" pagerank.txt))
    done
    
}

#Si le titre $1 n'est pas vide on cherche les ID
if test -n "$1" 
then
    ChercheID $1
fi

#print test
for val in ${IDPagerank[@]} 
do  
    echo $val
done

#awk -v a=$1 'BEGIN{var=a} ($2 ~ (a)) {print $1,$2}' id-titre.txt

exit 0

# commande1 | commande2 qui utilise le res1
# awk lis un res par ligne et colonne comme un tableau
#Titres = $()
#echo $Titres
#python3 fichier_list.py $1;