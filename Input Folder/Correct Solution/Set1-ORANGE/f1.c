
#include<stdio.h>
#include<stdlib.h>
#include "f1.h"



void rotateArray(int arr[], int n, int rotateBy) {
    // Adjust rotation value to handle negative and excessive rotations
    rotateBy = rotateBy % n;
    if (rotateBy < 0) {
        rotateBy = n + rotateBy;
    }

    // Temporary array to store rotated elements
    int temp[n];

    // Copy elements from the original array to the temporary array
    for (int i = 0; i < n; i++) {
        temp[i] = arr[i];
    }


    // Rotate the array elements by the given number of positions
    for (int i = 0; i < n; i++) {
        arr[(i + rotateBy) % n] = temp[i];
    }

}





