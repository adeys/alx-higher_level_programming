#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - check if a singly linked list is palindrome
 * @head: head of the list
 *
 * Return: 0 if @head is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *prev, *next, *start, *end;
	int list_len = 0, i = 0, is_pld = 1;

	if (*head == NULL || head == NULL)
		return (1);

	while (current != NULL)
		list_len++, current = current->next;

	if (list_len == 1)
		return (1);

	current = *head;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		next = current->next;
		current->next = prev;

		prev = current, current = next;
	}

	end = current, start = prev;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		if (list_len % 2 != 0 && i == 1)
			current = current->next;

		if (current->n != prev->n)
		{
			is_pld = 0;
			break;
		}

		current = current->next, prev = prev->next;
	}

	current = start, prev = end;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		prev = current, current = next;
	}

	return is_pld;
}
