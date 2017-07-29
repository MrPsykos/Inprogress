#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define WORDLENGTH 300000
#define NROFSTRINGS 300
void readFromFile(char fileName[],char *words[WORDLENGTH], int *readStrings);
int main()
{
    int readStrings = 0;
    char fileName[WORDLENGTH];
    char *words[WORDLENGTH];
    char **pointer2words = words;
    for (int i=0 ; i<WORDLENGTH; i++) {
        if ((words[i] = malloc(sizeof(char) * NROFSTRINGS)) == NULL) {
            printf("unable to allocate memory \n");
            return -1;
        }
    }


    readFromFile(fileName, words, &readStrings);
    printf("%d\n", readStrings);
    for(int i = 0; i< readStrings ; i++)
    {
        printf("%s",words[i]);
    }

}
void readFromFile(char fileName[], char *words[WORDLENGTH], int *readStrings)
{
    fileName = "data3.txt";
    FILE *fp;
    fp=fopen(fileName,"r");
    if(fp!=NULL)
    {
        int i = 0;
        while(fscanf(fp,"%s",words[i])==1)
        {
            strcat(words[i], "  ");
            i++;
            (*readStrings)++;
        }
    }
}
