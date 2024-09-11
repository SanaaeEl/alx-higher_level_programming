#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the first element of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node1, *node2;

	node1 = list;
	node2 = list;
	if (!list)
		return (0);

	while (list && list->next)
	{
		node1 = list->next;
		node2 = list->next->next;
		if (node1 == node2)
			return (1);	
	}
	return (0);
}
