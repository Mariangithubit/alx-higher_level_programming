#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info -  prints some basic info about Python lists
 * @p: pyobject
 */
void print_python_list_info(PyObject *p)
{
	int i;
	int size = pylist_size(p);
	PyObject *obj = (pyobject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0. i < size; i++)
		printf("Element %i: %s\n", i, py_type(obj_item[i])->tp_name);
}
