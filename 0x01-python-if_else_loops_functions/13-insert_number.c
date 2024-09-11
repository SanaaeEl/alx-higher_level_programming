#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: double pointer to the first element of the list
 * @number: number to be inserted
 * Return: pointer to the inserted element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (!temp)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;

	return (new);
}
