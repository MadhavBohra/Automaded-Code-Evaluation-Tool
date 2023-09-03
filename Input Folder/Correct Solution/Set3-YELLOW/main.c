#include <stdio.h>
#include "f1.h"
#include "f2.h"
#include "f3.h"

int main(int argc, char *argv[])
{

#if defined(F1_COMPILE)
     int size1, size2;

    printf("Enter the size of the first array: ");
    scanf("%d", &size1);

    int arr1[size1];

    printf("Enter the elements of the first array (in sorted order): ");
    for (int i = 0; i < size1; i++) {
        scanf("%d", &arr1[i]);
    }

    printf("Enter the size of the second array: ");
    scanf("%d", &size2);

    int arr2[size2];

    printf("Enter the elements of the second array (in sorted order): ");
    for (int i = 0; i < size2; i++) {
        scanf("%d", &arr2[i]);
    }

    int median = findMedian(arr1, size1, arr2, size2);

    printf("Median of the two arrays: %d \n", median);

    return 0;

#elif defined(F2_COMPILE)
    struct Node* head = NULL;

    int size, data;
    printf("Enter the size of the list: ");
    scanf("%d", &size);
    printf("Enter the elements of the list: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &data);
        head = insertNodeEnd(head, data);
    }

    printf("Original list: ");
    struct Node* current=head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");

    printf("Reversed linked list: ");

    struct Node *temp;
    temp=reverseLinkedList(head);

    while (temp != NULL) {
        printf("%d ", temp->data);
        temp= temp->next;
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
