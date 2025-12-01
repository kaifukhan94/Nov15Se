#include<stdio.h>

main(){
	
	float P,R,N,SI;
	
	printf("\n Enter Principal:");
	scanf("%f",&P);
	printf("\n Enter Rate of Interest:");
	scanf("%f",&R);
	printf("\n Enter Number of Years:");
	scanf("%f",&N);
	
	printf("\n Simple Interest: %f", (P*R*N)/100);
	
}
