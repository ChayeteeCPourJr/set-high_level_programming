#include <stdlib.h>
#include "lists.h"

/**
 * check_palindrome - recursively checks a list against a moving head
 * pointer, walking to the end of the list first via recursion, then
 * comparing values on the way back up as if from both ends inward
 * @left: pointer to a pointer that advances from the head of the list
 * @right: current node reached while recursing toward the tail
 *
 * Return: 1 if the sublist seen so far is a palindrome, 0 otherwise
 */
int check_palindrome(listint_t **left, listint_t *right)
{
	int result;

	if (right == NULL)
		return (1);

	result = check_palindrome(left, right->next);
	if (result == 0)
		return (0);

	if ((*left)->n != right->n)
		return (0);

	*left = (*left)->next;

	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *left;

	if (head == NULL || *head == NULL)
		return (1);

	left = *head;

	return (check_palindrome(&left, *head));
}
