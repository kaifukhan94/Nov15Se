#include<stdio.h>

main(){
	
	int a,b;
	
	printf("Enter first number:");
	scanf("%d",&a);
	printf("Enter second number:");
	scanf("%d",&b);
	
	printf("\n Addition: %d",a+b);
	printf("\n Subtraction: %d",a-b);
	printf("\n Multiplication: %d",a*b);
	printf("\n Division: %f",(float)a/b);
	printf("\n Remainder: %d",a%b);
}
