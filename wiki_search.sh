#!/bin/bash
#YOoo c'est le script de Tania et Bastien !!

ChercheID(){
    #Retourne les ID en lien avec le mot recherché
    ID=$(grep "\\b$1\\b" ./data/id-titre.txt | awk -F'\t' '{print $1}')
    
    #Retourne une liste avec (id1,valueid1,id2,valueid2, ...)
    IDPagerank=()
    for id in $ID
    do
        IDPagerank+=($(grep "^$id\\b" ./data/pagerank.txt))
    done

}

#Si le titre $1 n'est pas vide on cherche les ID
if test -n "$1"; then
    ChercheID $1

    #Si le titre retourne au moins un ID, on affiche le(s) meilleur(s)
    if test -n "$ID"; then  
        #Les ID sont triés par valeur du Pagerank et on retourne les 5 meilleurs
        BestId=$(./code/triPagerank ${IDPagerank[*]})
        
        #Affichage des 5 meilleurs
        i=1
        for id in $BestId
        do
            echo -n "$i >> " #Affiche le numéro 
            awk -v a=$id -F'\t' 'BEGIN{a++} NR == a {print $2}' ./data/id-titre.txt #Affiche le titre pour chaque ID
            i=$((i+1))
        done

        #Selection pour l'affichage du résumé
        echo "(Enter the number of the page wanted for a short summary)"

        read num 	#Lis le numéro tapé par l'utilisateur
        nbId=$(echo "^[1-"$(echo $BestId|wc -w)"]$") #Pour savoir si le numéro tapé est entre 1 et 5
        
        while ! [ $(echo $num | grep $nbId| wc -l) -eq "1" ]; do
            echo "Error : no matching title for \"$num\"" 
            read num
        done
        
        selection=$(echo $BestId | awk -v a=$num '{print $a}') #Prend la selection de l'utilisateur (ID)
        
        title=$(awk -v a=$selection -F'\t' 'BEGIN{a++} NR == a {print $0}' ./data/id-titre.txt) #Stocke le titre associé à la selection 
        
        python3 ./code/selecteur.py $title #On affiche le résumé de la selection
        echo "--"
        echo "Press i for more information on wikipedia"
        echo "Press q to quit"
        read info
        if [ $info = "i" ];then
            ./code/open_page $title
        fi
    else
        echo "Error : no result for «$1»."
    fi
else
    echo "Error : No argument."
    echo "wikiSearch expects a title suggestion for the search."
    echo "For example, try «./wikiSearch Hello»."
fi

#awk -v a=$1 'BEGIN{var=a} ($2 ~ (a)) {print $1,$2}' id-titre.txt

exit 0
