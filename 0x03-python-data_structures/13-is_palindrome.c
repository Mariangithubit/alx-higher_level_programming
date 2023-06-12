#include "lists.h"

/**
 * reverse_listint - reverse linked list
 * @head: the first node
 * Return: head
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL; 

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	temp = *head;
	size_t size = 0, j;

	if (!*head || (*head)->next == NULL)
		return (1);

	while (temp)
	{
		size++;
		temp = temp->next;
	}

	for (j = 0; j < (size / 2) - 1; j++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
