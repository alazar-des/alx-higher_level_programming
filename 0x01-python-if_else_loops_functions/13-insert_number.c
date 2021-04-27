#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node in a sorted linked list
 * @head: pointer to the head node pointer
 * @number: data to the new node
 *
 * Return: pointer to the new node if successful, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev = NULL, *temp = *head;

	if (head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		if ((*head)->n > number)
			break;
		prev = *head;
		*head = (*head)->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = *head;
	if (prev != NULL)
		prev->next = new;
	*head = temp;
	return (new);
}
