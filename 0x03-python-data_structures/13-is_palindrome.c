#include <stdlib.h>
#include "lists.h"

/**
 * len_list - return length of list
 * @head: pointer to head node
 * Return: length of node
 */
ssize_t len_list(listint_t *head)
{
	ssize_t count = 0;
	listint_t *h = head;

	while (head != NULL)
	{
		count++;
		head = head->next;
	}
	head = h;
	return (count);
}
/**
 * is_palindrome - check if list is palindrom
 * @head: pointer to the head node pointer
 *
 * Return: 1 if palindrom otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t **arr, *h;
	ssize_t n, i;

	if (head == NULL || *head == NULL)
		return (1);
	h = *head;
	n = len_list(*head);
	arr = malloc(sizeof(listint_t *) * n);
	if (arr == NULL)
		exit(EXIT_FAILURE);
	for (i = 0; i < n - 1; i++)
	{
		arr[i] = *head;
		*head = (*head)->next;
	}
	arr[n - 1] = *head;
	for (i = 0; i < n / 2; i++)
	{
		if (arr[i]->n != arr[n - 1 - i]->n)
			return (0);
	}
	if (arr != NULL)
		free(arr);
	*head = h;
	return (1);
}
