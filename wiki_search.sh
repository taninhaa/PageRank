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
if test -n "$1" 
then
    ChercheID $1

    if test -n "$IDPagerank"
    then  
        #Les ID sont triés par valeur du Pagerank
        BestId=$(./triPagerank ${IDPagerank[*]}|awk -F'\t' 'NR < 6 {print $1}')
        
        #On retourne les 5 meilleurs
        i=1
        for id in $BestId
        do
            echo -n "$i >> " 
            awk -v a=$id -F'\t' 'BEGIN{a++} NR == a {print $2}' id-titre.txt
            i=$((i+1))
        done
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
