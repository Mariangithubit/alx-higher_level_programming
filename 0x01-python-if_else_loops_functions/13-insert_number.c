#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linked list
 * @number: the value of new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	int n = 0;
	listint_t *n_node = NULL, *current = NULL, *after = NULL;

	if (!head)
		return (NULL);

	n_node = malloc(sizeof(listint_t));
	if (n_node == NULL)
		return (NULL);

	n_node->n = number, n_node->next = NULL;
	if (*head == NULL)
	{
		*head = n_node;
		return (*head);
	}

	current = *head;
	if (number <= current->n)
	{
		n_node->next = current, *head = n_node;
		return (*head);
	}

	if (number > current->n && !current->next)
	{
		current->next = n_node;
		return (n_node);
	}

	after = current->next;
	while (current)
	{
		if (after == NULL)
			current->next = n_node, n = 1;
		else if (after->n == number)
			current->next = n_node, n_node->next = after, n = 1;
		else if (after->n > number && current->n < number)
			current->next = n_node, n_node->next = after, n =  1;
		if (n)
			break;
		after = after->next, current = current->next;
	}
	return (n_node);
}
