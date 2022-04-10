#!/bin/bash
# Pour compiler chmod 755 nomfichier

#Test
echo Hello les copains

for ((i=1;i<20;i++))
do
    head -$(($(((RANDOM<<15)|RANDOM))% `wc -l < id-titre.txt` + 1)) id-titre.txt| tail -1
done


exit 0

# commande1 | commande2 qui utilise le res1
# awk lis un res par ligne et colonne comme un tableau
#Titres = $()
#echo $Titres
#python3 fichier_list.py $1;