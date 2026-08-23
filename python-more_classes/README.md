from pathlib import Path

readme = """# Python - More Classes

This project contains Python exercises focused on object-oriented programming, classes, properties, special methods, class attributes, static methods, class methods, and a backtracking algorithm.

## Files

| File | Description |
|---|---|
| `0-rectangle.py` | Defines an empty `Rectangle` class. |
| `1-rectangle.py` | Defines `Rectangle` with private `width` and `height` attributes, properties, setters, and validation. |
| `2-rectangle.py` | Adds `area()` and `perimeter()` methods to `Rectangle`. |
| `3-rectangle.py` | Adds string representation using the `#` character. |
| `4-rectangle.py` | Adds `__repr__()` so a rectangle can be recreated with `eval()`. |
| `5-rectangle.py` | Adds a deletion message and tracks the number of rectangle instances. |
| `6-rectangle.py` | Adds the public `print_symbol` class attribute used for string representation. |
| `7-rectangle.py` | Adds the static method `bigger_or_equal()` to compare two rectangles by area. |
| `8-rectangle.py` | Adds the class method `square()` to create a square-shaped rectangle. |
| `101-nqueens.py` | Solves the N Queens puzzle using a backtracking algorithm. |

## `0-rectangle.py`

Creates an empty `Rectangle` class.

```python
class Rectangle:
    pass

1-rectangle.py

Adds:

Private width and height attributes.
width and height properties.
Validation for integer values.
Validation for values greater than or equal to zero.
Optional width and height parameters.
2-rectangle.py

Adds:

area() to calculate the rectangle area.
perimeter() to calculate the rectangle perimeter.
A perimeter of 0 when either dimension is 0.
3-rectangle.py

Adds __str__() so the rectangle is displayed using #.

For example:

####
####
####

If either dimension is 0, an empty string is returned.

4-rectangle.py

Adds __repr__().

The returned representation can be used with eval() to create another Rectangle instance.

Example:

r = Rectangle(4, 3)
print(repr(r))

Output:

Rectangle(4, 3)
5-rectangle.py

Adds:

number_of_instances class attribute.
Incrementing of the instance count when a rectangle is created.
Decrementing of the instance count when a rectangle is deleted.
__del__() with the message:
Bye rectangle...
6-rectangle.py

Adds the class attribute:

print_symbol = "#"

The symbol can be changed to another value and is used by __str__().

7-rectangle.py

Adds the static method:

bigger_or_equal(rect_1, rect_2)

It:

Checks that both arguments are Rectangle instances.
Raises the required TypeError messages for invalid arguments.
Returns the rectangle with the larger area.
Returns rect_1 when both rectangles have the same area.
8-rectangle.py

Adds the class method:

square(size=0)

It creates and returns a new Rectangle where:

width == height == size

Example:

square = Rectangle.square(5)
print(square.width)
print(square.height)

Output:

5
5
101-nqueens.py

Solves the N Queens puzzle.

Usage
./101-nqueens.py N

N must be an integer greater than or equal to 4.

Error handling

If the number of arguments is incorrect:

Usage: nqueens N

If N is not an integer:

N must be a number

If N is less than 4:

N must be at least 4
Algorithm

The program uses backtracking to place one queen on each row while ensuring that no two queens share:

A column.
A diagonal.

Only the sys module is imported.

Example:

./101-nqueens.py 4

Possible output:

[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
Requirements
Python 3
No external Python modules.
The rectangle exercises do not require imports.
101-nqueens.py uses only the sys module.
