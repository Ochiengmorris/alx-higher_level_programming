#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.      * @lt: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *lt)
{
	listint_t *current, *check;

	if (lt == NULL || lt->next == NULL)
		return (0);
	current = lt;
	check = current->next;

	while (current != NULL && check->next != NULL
			&& check->next->next != NULL)
{
	if (current == check)
		return (1);
	current = current->next;

	check = check->next->next;
}
	return (0);
}

