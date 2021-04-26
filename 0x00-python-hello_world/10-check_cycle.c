#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if cycle exist in single linked list
 * @list: pointer to the head node of the list
 *
 * Return: if cycle does not exit 0, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *next_list;

	current = list;
	if (list != NULL)
		next_list = list->next;
	while (current != NULL)
	{
		if (current == next_list)
			return (1);
		if (next_list->next == NULL)
			break;
		next_list = (next_list->next)->next;
		current = current->next;
	}
	return (0);
}
