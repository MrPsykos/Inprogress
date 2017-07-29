#include <stdio.h>
#include <string.h>
#define WORDLENGTH 30
#define NROFSTRINGS 10000
void readFromFile(char fileName[],char strings[WORDLENGTH][NROFSTRINGS]);
int main()
{
	    char fileName[WORDLENGTH];
	    char strings[WORDLENGTH][NROFSTRINGS];	
	    readFromFile(fileName, strings[NROFSTRINGS]);
	    for(int i = 0; i < NROFSTRINGS-1;i++)
	    {
	    	printf("%s\n",strings[i]);
	    }
	
	return 0;
}
void readFromFile(char fileName[], char strings[WORDLENGTH][NROFSTRINGS])
{
	printf("Hello");
	sprintf(fileName,"data.txt",fileName);
	
	FILE *fp;
	fp=fopen(fileName,"r");
	if(fp!=NULL)
    {
    	int i = 0;
    	char a[WORDLENGTH];
    	while(fscanf(fp,"%s",a != '\0'))
    	{
    		strings[i][0] = a;
    		i++;
    	}
    }
}