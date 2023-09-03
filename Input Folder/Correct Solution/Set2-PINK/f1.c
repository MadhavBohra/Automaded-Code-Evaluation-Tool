
#include<stdio.h>
#include<stdlib.h>
#include "f1.h"


int * minarray(int A[], int n){

int *G=(int *)malloc(sizeof(int)*n);

for (int i = 0; i < n; i++) {
        int j = i - 1;
        while (j >= 0 && A[j] >= A[i]) {
            j--;
        }
        if (j >= 0) {
            G[i] = A[j];
        } else {
            G[i] = -1;  // No smaller element found
        }
    }

   return G;


}


