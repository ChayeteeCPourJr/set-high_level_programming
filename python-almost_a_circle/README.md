# Python - Almost a Circle

## Description

This project practices Python object-oriented programming, inheritance,
data validation, serialization, deserialization, and testing. It builds
a model system using a `Base` class and its `Rectangle` and `Square`
subclasses.

## Learning Objectives

-   Create classes and use inheritance.
-   Manage instance and class attributes.
-   Validate attributes with properties and setters.
-   Use `*args` and `**kwargs` to update objects.
-   Convert objects to dictionaries and JSON strings.
-   Save and load objects using JSON and CSV.
-   Write tests and follow Python style conventions.

## Project Structure

``` text
python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
├── tests/
│   └── ...
└── README.md
```

The repository may also contain numbered main files used to test
individual tasks.

## Classes

### `Base`

The `Base` class manages object IDs and shared serialization utilities.

-   `__init__(id=None)` --- initializes an instance ID.
-   `to_json_string(list_dictionaries)` --- converts a list of
    dictionaries to JSON text.
-   `from_json_string(json_string)` --- converts JSON text back into a
    Python list.
-   `save_to_file(list_objs)` --- saves objects to `<ClassName>.json`.
-   `load_from_file()` --- loads objects from `<ClassName>.json`.
-   `create(**dictionary)` --- creates an instance and applies
    attributes through `update()`.
-   `save_to_file_csv(list_objs)` --- saves objects to
    `<ClassName>.csv`.
-   `load_from_file_csv()` --- loads objects from `<ClassName>.csv`.
-   `draw(list_rectangles, list_squares)` --- draws shapes with Turtle
    graphics when a graphical environment is available.

### `Rectangle`

`Rectangle` inherits from `Base`. It represents a rectangle and supports
width, height, x and y attributes, area calculation, display, string
representation, attribute updates, and conversion to a dictionary.

### `Square`

`Square` inherits from `Rectangle`. Its size is used for both width and
height. It supports display, string representation, updates, and
conversion to a dictionary.

## Requirements

-   Python 3
-   No external packages are required for the core model classes.
-   Turtle drawing may require a graphical desktop environment and Tk
    support.

Check your Python version:

``` bash
python3 --version
```

## Usage

Run commands from the project directory.

### Create objects

``` python
from models.rectangle import Rectangle
from models.square import Square

rectangle = Rectangle(10, 7, 2, 8)
square = Square(5, 1, 2)

print(rectangle)
print(rectangle.area())
print(square)
print(square.area())
```

### Save and load JSON

``` python
from models.rectangle import Rectangle

rectangle = Rectangle(10, 7, 2, 8)
Rectangle.save_to_file([rectangle])

loaded_rectangles = Rectangle.load_from_file()
for item in loaded_rectangles:
    print(item)
```

The JSON filename is based on the class name, such as `Rectangle.json`.

### Save and load CSV

``` python
from models.square import Square

square = Square(5, 1, 2)
Square.save_to_file_csv([square])

loaded_squares = Square.load_from_file_csv()
for item in loaded_squares:
    print(item)
```

CSV row formats:

-   Rectangle: `id,width,height,x,y`
-   Square: `id,size,x,y`

## Running Tests

If the repository contains a `tests/` directory, run the tests from the
project root:

``` bash
python3 -m unittest discover tests
```

Run a numbered example file using its actual filename, for example:

``` bash
python3 15-main.py
```

### Syntax and style checks

``` bash
python3 -m py_compile models/base.py
```

If `pycodestyle` is installed:

``` bash
pycodestyle models/
```

## Notes

-   Run commands from the repository root so JSON and CSV files are
    created in the expected directory.
-   Loading methods return an empty list when the expected file does not
    exist.
-   CSV loading expects numeric values in the specified column order.
-   `create()` relies on each subclass's `update()` method.
-   For Turtle drawing in WSL, make sure a graphical display and Tk
    support are available.

## Author

Add your name or GitHub username here.
