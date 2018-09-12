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
	listint_t *trav2;
	listint_t *tmp;

	trav = *head;

	tmp = malloc(sizeof(listint_t));
	if (!tmp)
		return (NULL);

	tmp->n = number;
	tmp->next = NULL;

	if (*head == NULL)
	{
		*head = tmp;
		return (tmp);
	}

	if (trav->next == NULL)
	{
		if (trav->n < number)
		{
			trav->next = tmp;
			return (*head);
		}
		else
		{
			tmp->next = trav;
			*head = tmp;
			return (tmp);
		}
	}

	while (trav)
	{
		trav2 = trav->next;
		if (trav->n > number)
		{
			tmp->next = trav;
			*head = tmp;
			return (tmp);
		}
		else if ((trav->n < number) && (trav2->n < number))
		{
			trav = trav->next;
			trav2 = trav2->next;
		}
		else if ((trav->n < number) && (trav2->n >= number))
		{
			tmp->next = trav2;
			trav->next = tmp;
			break;
		}
		else if ((trav->n < number) && (trav2->next == NULL))
		{
			tmp->next = NULL;
			trav2->next = tmp;
			break;
		}
	}
	return (trav);
}
