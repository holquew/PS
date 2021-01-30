#include<stdio.h>

typedef enum{ false, true}bool;
bool star[3072][6144] = {false,};
int n, i,j,k;
int w;

void checkstar( )
{
	int nowW;
	int mid = w / 2;
	
	star[0][w / 2] = star[1][w / 2 - 1] = star[1][w / 2 + 1] = true;
	for(i = -2; i < 3; i++)
		star[2][w / 2 + i] = true;
	
	for(i = 3; i != n; i *= 2)
	{
		nowW = i * 2 - 1;
		for(k = 0; k < i; k++)
			for(j = 0; j < nowW; j++)
				star[i+k][mid-nowW+j] = star[i+k][mid+1+j] = star[k][mid-nowW/2+j];
	}
}
int main( )
{
	scanf("%d", &n);
	w = 2 * n - 1;
	checkstar( );
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < w; j++)
			star[i][j] ? printf("*") : printf(" ");
		printf("\n");
	}
	return 0;
}