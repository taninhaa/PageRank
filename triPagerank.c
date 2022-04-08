#include <stdio.h>
#include <stdlib.h>

void affiche_tab(float** tab, int N){//ex1
    for(int i=0;i<N;i++)
        printf("%.0f\t%.15f\n",tab[i][0],tab[i][1]);
}

float** nouveau_tableau(int N){
    //alloue de la mémoire pour un tableau[2][N] de float
    float** tab = (float**) malloc(N * sizeof(float*));
    for(int i=0; i<N ; i++)
        tab[i] = (float*) malloc(2*sizeof(float));

    return tab;
}

void detruire_tableau(float **tab,int N){
    for(int i=0; i<N ; i++) 
        free(tab[i]);
    free(tab);
}

void tri_rapide(float** tab, int N){
    if(N!=1 && N!=0){
        int indice_pivot = rand()%N;// un élément quelconque d'indice aléatoire
        float pivot = tab[indice_pivot][1];
        float valpivot = tab[indice_pivot][0];
        int indice_inf = 0;// le nombre d'élément dans la liste d'élément inférieur ou égale au pivot
        int indice_sup = 0;// le nombre d'élément dans la liste d'élément supérieur au pivot

        for(int i=0;i<N;i++){// on compte le nombre d'élément <=  et > au pivot
            if(i!=indice_pivot){
                if(tab[i][1]<=pivot)
                    indice_inf++;
                if(tab[i][1]>pivot)//else
                    indice_sup++;
            }
        }
        // on créé les deux sous ensembles avec la taille approprié
        float** tab_inferieur = nouveau_tableau(indice_inf);
        float** tab_superieur = nouveau_tableau(indice_sup);

        indice_inf = 0;
        indice_sup = 0;
        
        // on remplit les sous ensembles/listes
        for(int i=0;i<N;i++){
            if(i!=indice_pivot){
                if(tab[i][1]<=pivot){
                    tab_inferieur[indice_inf][0]=tab[i][0];
                    tab_inferieur[indice_inf][1]=tab[i][1];
                    indice_inf++;
                }
                if(tab[i][1]>pivot){//else
                    tab_superieur[indice_sup][0]=tab[i][0];
                    tab_superieur[indice_sup][1]=tab[i][1];
                    indice_sup++;
                }    
            }
        }
        // Appel récursif sur les sous ensembles <= et >
        if(indice_inf!=0){
            tri_rapide(tab_inferieur,indice_inf);
        }
        if(indice_sup!=0){
            tri_rapide(tab_superieur,indice_sup);
        }
        
        //Les tableaux sont triés par l'appel récurssif
        //il suffit de recopier les éléments dans l'ordre
        for(int i=0;i<N;i++){
            if(i<indice_inf){// on commence par la liste <=
                tab[i][0] = tab_inferieur[i][0];
                tab[i][1] = tab_inferieur[i][1];
            }
            else{
                if(i==indice_inf){//puis le pivot
                    tab[i][0] = valpivot;
                    tab[i][1] = pivot;
                }else{//enfin la liste > au pivot
                    tab[i][1]=tab_superieur[i-indice_inf-1][0];
                    tab[i][1]=tab_superieur[i-indice_inf-1][1];
                }
            }
        }
        //on désalloue la mémoire
        detruire_tableau(tab_inferieur,indice_inf);
        detruire_tableau(tab_superieur,indice_sup);
    }
}

int main (int argc, char *argv[]){
    if (argc == 1){
        printf("Pas de resultat\n");
        return 0;
    }
    int taille_tab = (argc-1)/2;
    float** tab = nouveau_tableau(taille_tab);
    for(int i=0;i<taille_tab;i++){
        tab[i][0] = atof(argv[2*i+1]);
        tab[i][1] = atof(argv[2*i+2]);
    }
    
    tri_rapide(tab,taille_tab);
    affiche_tab(tab,taille_tab);
    detruire_tableau(tab,taille_tab);
    return 0;
}