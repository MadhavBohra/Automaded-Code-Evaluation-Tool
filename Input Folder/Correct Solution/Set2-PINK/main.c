#include <stdio.h>
#include "f1.h"
#include "f2.h"
#include "f3.h"

int main(int argc, char *argv[])
{

#if defined(F1_COMPILE)
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int A[n];
    int *G;
    printf("Enter the elements of the array:");
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
    }

    G=minarray(A, n);
    printf("The array containing nearest smaller elements:");
    for (int i = 0; i < n; i++) {
        printf("%d ", G[i]);
    }
    printf("\n");
    return 0;



#elif defined(F2_COMPILE)
    struct Node* head = NULL;

    int size, data;
    printf("Enter the size of the list: ");
    scanf("%d", &size);
    if(size==0)
        {
            printf("No elements can be taken \n ");
    }
    else{
    printf("Enter the elements of the list: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &data);
        head = insertNode(head, data);
    }
    }

    printf("Original list: ");

    struct Node *temp=head;

    while (temp != NULL) {
        printf("%d ", temp->data);
        temp= temp->next;
    }
    printf("\n");
    struct Node* middleNode = findMiddle(head);

    if (middleNode != NULL)
        printf("Middle element: %d\n", middleNode->data);
    else
        printf("There does not exist any middle element\n");

     return 0;

#elif defined(F3_COMPILE)
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    pattern(n);

#endif

    return 0;
}
