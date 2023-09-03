
#include <stdio.h>
#include <stdlib.h>

#include "f2.h"

 struct Node* reverseLinkedList(struct Node* head) {
    struct Node* current = head;
    struct Node* previous = NULL;
    struct Node* next = NULL;

    while (current != NULL) {
        next = current->next;  // Store the next node
        current->next = previous;  // Reverse the link

        // Move pointers one position ahead
        previous = current;
        current = next;
    }

    return previous;  // New head of the reversed list
}

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



