
#include <stdio.h>
#include "f3.h"

void pattern(int n)
{
         int  i, j, space;
       for (i = 0; i < n; i++) {
        for (space = 0; space < n - i - 1; space++) {
            printf(" ");
        }
        printf("*");
        for (j = 0; j < 2 * i - 1; j++) {
            printf(" ");
        }
        if (i != 0) {
            printf("*");
        }
        printf("\n");
    }


    for (i = n - 2; i >= 0; i--) {
        for (space = 0; space < n - i - 1; space++) {
            printf(" ");
        }
        printf("*");
        for (j = 0; j < 2 * i - 1; j++) {
            printf(" ");
        }
        if (i != 0) {
            printf("*");
        }
        printf("\n");
    }


}
