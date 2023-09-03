
#include<stdio.h>
#include "f1.h"





int findMedian(int arr1[], int size1, int arr2[], int size2) {
    int totalSize = size1 + size2;
    int mergedArray[totalSize];
    int i = 0, j = 0, k = 0;

    while (i < size1 && j < size2) {
        if (arr1[i] < arr2[j]) {
            mergedArray[k] = arr1[i];
            i++;
        } else {
            mergedArray[k] = arr2[j];
            j++;
        }
        k++;
    }

    while (i < size1) {
        mergedArray[k] = arr1[i];
        i++;
        k++;
    }

    while (j < size2) {
        mergedArray[k] = arr2[j];
        j++;
        k++;
    }

    int medianIndex = totalSize / 2;
    int median;

    if (totalSize % 2 == 0) {
        median = (mergedArray[medianIndex - 1] + mergedArray[medianIndex]) / 2.0;
    } else {
        median = mergedArray[medianIndex];
    }

    return median;
}
