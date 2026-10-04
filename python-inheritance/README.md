from pathlib import Path

readme = """# Python Inheritance

This directory contains exercises focused on **Python inheritance**, classes, methods, validation, and special methods.

## Files

| File | Description |
|---|---|
| `0-lookup.py` | Defines `lookup(obj)` to return a list of an object's available attributes and methods. |
| `1-my_list.py` | Defines `MyList`, a subclass of `list`, with a `print_sorted()` method. |
| `2-is_same_class.py` | Defines `is_same_class(obj, a_class)` to check whether an object is exactly an instance of a specified class. |
| `3-is_kind_of_class.py` | Defines `is_kind_of_class(obj, a_class)` to check whether an object is an instance of a class or one of its subclasses. |
| `4-inherits_from.py` | Defines `inherits_from(obj, a_class)` to check whether an object is an instance of a subclass of a specified class. |
| `5-base_geometry.py` | Defines an empty `BaseGeometry` class. |
| `6-base_geometry.py` | Defines `BaseGeometry` with an `area()` method and an `integer_validator()` method. |
| `7-base_geometry.py` | Defines `BaseGeometry` with an `area()` method that raises an exception when it is not implemented. |
| `8-rectangle.py` | Defines `Rectangle`, which inherits from `BaseGeometry`, validates dimensions, and calculates area. |
| `9-rectangle.py` | Extends `Rectangle` with an implemented `area()` method and a rectangle string representation. |
| `10-square.py` | Defines `Square`, which inherits from `Rectangle` and implements square area calculation. |
| `11-square.py` | Extends `Square` with an implemented `area()` method and square string representation. |
| `100-my_int.py` | Defines `MyInt`, a subclass of `int` with inverted `==` and `!=` behavior. |
| `101-add_attribute.py` | Defines `add_attribute()` to add an attribute to an object when possible. |

## Concepts Covered

### 1. Object Inspection
`lookup()` uses Python's built-in `dir()` function to retrieve available attributes and methods.

### 2. Inheritance
Several classes demonstrate how one class can inherit behavior from another:

```python
class Square(Rectangle):
    pass

3. Type Checking

The exercises demonstrate the difference between:

type(obj) is a_class — checks for an exact class match.
isinstance(obj, a_class) — checks for an instance of a class or its subclasses.
4. Validation

BaseGeometry.integer_validator() validates that a value is:

an integer
greater than 0

It raises:

TypeError: <name> must be an integer

or:

ValueError: <name> must be greater than 0
5. Special Methods

The project uses special methods such as:

__init__() — initializes objects.
__str__() — controls the string representation of an object.
__eq__() — controls equality comparison.
__ne__() — controls inequality comparison.
6. Private Attributes

Rectangle and Square use private attributes:

self.__width
self.__height
self.__size

These attributes cannot be accessed directly using their normal names from outside the class.

Example

A Rectangle can be created and displayed as follows:

rectangle = Rectangle(3, 4)

print(rectangle)
print(rectangle.area())

Expected output:

[Rectangle] 3/4
12

A Square can be used similarly:

square = Square(5)

print(square)
print(square.area())

Expected output:

[Square] 5/5
25
Requirements
Python 3
No external modules are required.
The solutions should follow PEP 8 / Pycodestyle conventions.
Each file should include appropriate documentation.
Testing

Individual files can be tested with their corresponding test scripts.

Pycodestyle can be run with:

pycodestyle *.py
Repository Structure
python-inheritance/
├── 0-lookup.py
├── 1-my_list.py
├── 2-is_same_class.py
├── 3-is_kind_of_class.py
├── 4-inherits_from.py
├── 5-base_geometry.py
├── 6-base_geometry.py
├── 7-base_geometry.py
├── 8-rectangle.py
├── 9-rectangle.py
├── 10-square.py
├── 11-square.py
├── 100-my_int.py
├── 101-add_attribute.py
└── README.md

Author

