#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: the head of new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *trav;
	listint_t *node;

	trav = *head;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	if (trav->next == NULL)
	{
		if (trav->n < number)
		{
			trav->next = node;
			return (node);
		}
		else
		{
			node->next = trav;
			*head = node;
			return (node);
		}
	}

	while (trav)
	{
		if (trav->next)
		{
			if (trav->next->n > number)
			{
				node->next = trav->next;
				trav->next = node;
				break;
		    }
			else
				trav = trav->next;
		}
		else
		{
			node->next = NULL;
			trav->next = node;
			break;
		}
	}
	return (node);
}
