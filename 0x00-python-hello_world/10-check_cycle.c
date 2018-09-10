#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *once;
	listint_t *twice;
	once = list;
	twice = list;

	while (twice)
	{
		once = once->next;
		twice = twice->next;
		twice = twice->next;
		if (once == twice)
			return (1);
	}
	return (0);
}
