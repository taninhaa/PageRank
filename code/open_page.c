#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main (int argc,char* argv[]){
    char* url = (char*) malloc(100*sizeof(char));
    url[0] = '\0';
    strcat(url,"xdg-open \"https://en.wikipedia.org/wiki/");
    for (int i = 2; i < argc; i++){
        strcat(url,argv[i]);
        if(i!=argc-1)
            strcat(url,"_");
        else
            strcat(url,"\"");
    }

    if (system(url) != 0)
        printf("Error command : %s\n",url);
    
    free(url);
    return 0;
}