#!/bin/bash
#YOoo c'est le script de Tania et Bastien !!

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
if test -n "$1"; then
    ChercheID $1

    #Si le titre retourne au moins un ID, on affiche le(s) meilleur(s)
    if test -n "$ID"; then  
        #Les ID sont triés par valeur du Pagerank et on retourne les 5 meilleurs
        BestId=$(./triPagerank ${IDPagerank[*]})
        
        #Affichage des 5 meilleurs
        i=1
        for id in $BestId
        do
            echo -n "$i >> " 
            awk -v a=$id -F'\t' 'BEGIN{a++} NR == a {print $2}' id-titre.txt
            i=$((i+1))
        done

        #Selection pour l'affichage du résumé
        echo "(Entrez le numéro associé au titre pour afficher un court résumé)"
        read num
        nbId=$(echo "^[1-"$(echo $BestId|wc -w)"]$")
        while ! [ $(echo $num | grep $nbId| wc -l) -eq "1" ]; do
            echo "Erreur : \"$num\" ne correspond à aucun titre" 
            read num
        done
        
        selection=$(echo $BestId | awk -v a=$num '{print $a}')
        
        title=$(awk -v a=$selection -F'\t' 'BEGIN{a++} NR == a {print $0}' id-titre.txt)
        
        python3 selecteur.py $title
    else
        echo "Erreur : «$1» ne retourne aucun résultat."
    fi
else
    echo "Erreur : Aucun argument."
    echo "wikiSearch attend une suggestion de titre pour la recherche."
    echo "Par exemple, essayez «./wikiSearch chat»."
fi

#awk -v a=$1 'BEGIN{var=a} ($2 ~ (a)) {print $1,$2}' id-titre.txt

exit 0
