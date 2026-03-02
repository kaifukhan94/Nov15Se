//ASSESSMENT
#include <stdio.h>

// Function declaration
void multiply(int a[2][2], int b[2][2], int c[2][2]);

int main() {
    int a[2][2], b[2][2], c[2][2];
    int i, j;

    // Input first matrix
    printf("Enter elements of Matrix 1:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    // Display first matrix
    printf("\nMatrix 1:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    // Input second matrix
    printf("\nEnter elements of Matrix 2:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            scanf("%d", &b[i][j]);
        }
    }

    // Display second matrix
    printf("\nMatrix 2:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }

    // Function call
    multiply(a, b, c);

    // Display result matrix
    printf("\nResultant Multiplication Matrix:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }

    return 0;
}

// Function definition
void multiply(int a[2][2], int b[2][2], int c[2][2]) {
    int i, j, k;

    // Initialize result matrix
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            c[i][j] = 0;
        }
    }

    // Matrix multiplication logic
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            for (k = 0; k < 2; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

