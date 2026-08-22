#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about a Python list
 * @p: a PyObject pointer to a Python list
 *
 * Description: prints the list's size, the number of allocated
 * slots, and the type name of each element it contains.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloc, i;
	const char *type_name;

	size = Py_SIZE(list);
	alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		type_name = Py_TYPE(list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}
