#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the first node of listint_t list
 * @number: integer to be included in the new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *updated_node, *current, *previous;

updated_node = malloc(sizeof(listint_t));
if (updated_node == NULL)
return (NULL);

updated_node->n = number;
updated_node->next = NULL;
current = *head;
previous = NULL;

while (current != NULL && current->n < number)
{
previous = current;
current = current->next;
}

if (previous == NULL)
{
updated_node->next = *head;
*head = updated_node;
}
else
{
updated_node->next = current;
previous->next = updated_node;
}

return (updated_node);
}
