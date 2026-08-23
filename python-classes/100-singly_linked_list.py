#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class"""


class Node:
    """Represents a node of a singly linked list

    Attributes:
        __data (private): the integer value stored in the node
        __next_node (private): the next Node in the list, or None
    """

    def __init__(self, data, next_node=None):
        """Initialize a new Node

        Args:
            data: the integer value to store
            next_node: the next Node in the list (default None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in this node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in this node

        Args:
            value: the new data value

        Raises:
            TypeError: if value is not an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list

        Args:
            value: the next Node, or None

        Raises:
            TypeError: if value is neither None nor a Node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list of Node objects

    Attributes:
        __head (private): the first Node of the list, or None
    """

    def __init__(self):
        """Initialize a new, empty SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the list, keeping it sorted
        in increasing order

        Args:
            value: the integer value to insert
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string with each node's data on its own line"""
        lines = []
        current = self.__head
        while current is not None:
            lines.append(str(current.data))
            current = current.next_node
        return "\n".join(lines)
