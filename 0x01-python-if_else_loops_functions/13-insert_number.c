#include "lists.h"
/**
 * insert_node - inserts a node int a linked list
 * @head: the head pointer
 * @number: the number to be inserted
 * Return: address of the new node or NULL if fail
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *prev_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	prev_node = *head;
	current_node = (*head)->next;
	
	while (current_node != NULL && current_node->n < number)
	{
		prev_node = current_node;
		current_node = current_node->next;
	}

	prev_node->next = new_node;
	new_node->next = current_node;

	return (new_node);
}


