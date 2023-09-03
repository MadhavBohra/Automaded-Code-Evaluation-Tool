
#include <stdio.h>
#include "f3.h"

void pattern(int n)
{
int i,j, space;
for (int i = 0; i < n; i++) {
        for (space = 0; space < n - i - 1; space++) {
            printf(" ");
        }
        for (j = 0; j <= i; j++) {
            if (j == 0 || j == i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }

    for (i = n - 2; i >= 0; i--) {
        for (space = 0; space < n - i - 1; space++) {
            printf(" ");
        }
        for (j = 0; j <= i; j++) {
            if (j == 0 || j == i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }

}
