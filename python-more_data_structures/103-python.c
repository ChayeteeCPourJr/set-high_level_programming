#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - prints basic info about a Python bytes object
 * @p: a PyObject pointer, expected to be a bytes object
 *
 * Description: prints the size of the bytes object, attempts to
 * print it as a string, and prints (up to 10) of its raw bytes in
 * hexadecimal. If p is not a valid bytes object, prints an error
 * message instead.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t size, nb_bytes, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = bytes->ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	nb_bytes = size + 1;
	if (nb_bytes > 10)
		nb_bytes = 10;

	printf("  first %ld bytes: ", nb_bytes);
	for (i = 0; i < nb_bytes; i++)
	{
		printf("%02x", bytes->ob_sval[i] & 0xff);
		if (i < nb_bytes - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - prints basic info about a Python list
 * @p: a PyObject pointer, expected to be a list object
 *
 * Description: prints the list's size, the number of allocated
 * slots, and the type name of each element. If an element is a
 * bytes object, also prints its detailed bytes info.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloc, i;
	const char *type_name;
	PyObject *element;

	size = list->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		element = list->ob_item[i];
		type_name = element->ob_type->tp_name;

		printf("Element %ld: %s\n", i, type_name);

		if (strcmp(type_name, "bytes") == 0)
			print_python_bytes(element);
	}
}
