#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int arr[3000], count = 0;
	int i, j;
	listint_t *tmp;
	
	tmp = *head;

	if (!head)
		return (0);

	while (tmp)
	{
		arr[count] = tmp->n;
		tmp = tmp->next;
		count++;
	}

	for (i = 0, j = count - 1; i < count / 2 + 1; i++, j--)
		if (arr[i] != arr[j])
			return (0);

	return (1);
}
