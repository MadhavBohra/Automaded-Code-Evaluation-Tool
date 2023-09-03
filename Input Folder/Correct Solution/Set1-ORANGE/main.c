#include <stdio.h>
#include <stdlib.h>
#include "f1.h"
#include "f2.h"
#include "f3.h"

int main(int argc, char *argv[])
{
#if defined(F1_COMPILE)
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int Arr[n];


    printf("Enter the elements of the array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &Arr[i]);}

    int rotateBy;
    printf("Enter the number of positions to rotate (positive or negative): ");
    scanf("%d", &rotateBy);

    rotateArray(Arr, n, rotateBy);

    printf("Rotated array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", Arr[i]);
    }
    printf("\n");


#elif defined(F2_COMPILE)
    struct Node* head1 = NULL;
    struct Node* head2 = NULL;

    int size1, size2, data;
    printf("Enter the size of list 1 and list 2: ");
    scanf("%d %d", &size1, &size2);

    printf("Enter the elements of list 1: ");
    for (int i = 0; i < size1; i++) {
        scanf("%d", &data);
        head1 = insertNodeEnd(head1, data);
    }

    printf("Enter the elements of list 2 : ");
    for (int i = 0; i < size2; i++) {
        scanf("%d", &data);
        head2 = insertNodeEnd(head2, data);
    }

    printf("List 1: ");
    struct Node* current1 = head1;
    while (current1 != NULL) {
        printf("%d ", current1->data);
        current1 = current1->next;
    }
    printf("\n");
    printf("List 2: ");
    struct Node* current2 = head2;
    while (current2 != NULL) {
        printf("%d ", current2->data);
        current2 = current2->next;
    }
    printf("\n");

    struct Node *common= (struct Node*)malloc(sizeof(struct Node));
    common=printCommonElements(head1, head2);
    struct Node* current3 = common;
    if (current3 == NULL) {
        printf("No common elements");
    }
    else{
    printf("New Link list created of common elements:");

    while (current3 != NULL) {
        printf("%d ", current3->data);
        current3 = current3->next;
    }
    }
    printf("\n");



    return 0;

#elif defined(F3_COMPILE)
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    pattern(n);

#endif

    return 0;
}
