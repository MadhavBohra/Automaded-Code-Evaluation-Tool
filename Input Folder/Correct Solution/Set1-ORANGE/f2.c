
#include <stdio.h>
#include <stdlib.h>

#include "f2.h"




struct Node* insertNodeEnd(struct Node* head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
    } else {
        struct Node* current = head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }

    return head;
}




struct Node* printCommonElements(struct Node* head1, struct Node* head2) {
    int foundCommonElement = 0;
    struct Node* commonHead = NULL;
    struct Node* temp1 = head1;
    while (temp1 != NULL) {
        struct Node* temp2 = head2;
        while (temp2 != NULL) {
            if (temp1->data == temp2->data) {
                //printf("%d ", temp1->data);
                commonHead = insertNodeEnd(commonHead, temp1->data);
                  // Set the flag to indicate a common element is found
                  foundCommonElement = 1;
                   break;

            }
            temp2 = temp2->next;
        }
        temp1 = temp1->next;
    }

    return(commonHead);
}




