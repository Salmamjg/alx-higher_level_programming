#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer of the first node
 * Return: 1 if palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
listint_t *slow, *fast, *prev, *temp;
listint_t *half, *mid;

slow = fast = *head;
prev = NULL;

while (fast && fast->next)
{
fast = fast->next-> next;
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}

if (fast)
{
mid = slow;
slow = slow->next;
}
half = slow;
prev = NULL;





}


