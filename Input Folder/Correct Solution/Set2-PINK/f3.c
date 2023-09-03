
#include <stdio.h>
#include "f3.h"

void pattern(int n)
{

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j == i || j == n - i - 1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }

    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < n; j++) {
            if (j == i || j == n - i - 1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }


}
