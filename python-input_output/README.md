from pathlib import Path

readme = """# Python Input/Output

This directory contains Python exercises focused on file handling, JSON serialization/deserialization, classes, and log parsing.

## Files

### `3-to_json_string.py`
Converts a Python object into its JSON string representation.

- Function: `to_json_string(my_obj)`
- Uses `json.dumps()`.

### `4-from_json_string.py`
Converts a JSON string into a Python object.

- Function: `from_json_string(my_str)`
- Uses `json.loads()`.

### `5-save_to_json_file.py`
Writes a Python object to a text file using JSON representation.

- Function: `save_to_json_file(my_obj, filename)`
- Uses `json.dump()`.
- Uses the `with` statement.

### `6-load_from_json_file.py`
Loads a Python object from a JSON file.

- Function: `load_from_json_file(filename)`
- Uses `json.load()`.
- Uses the `with` statement.

### `7-add_item.py`
Adds command-line arguments to a list and saves the list in `add_item.json`.

- Uses `save_to_json_file()` from `5-save_to_json_file.py`.
- Uses `load_from_json_file()` from `6-load_from_json_file.py`.
- Creates `add_item.json` if it does not already exist.

### `8-class_to_json.py`
Returns the dictionary representation of an object for JSON serialization.

- Function: `class_to_json(obj)`
- Uses `obj.__dict__`.
- Does not import any module.

### `9-student.py`
Defines a `Student` class with:

- `first_name`
- `last_name`
- `age`
- `to_json()` method

### `10-student.py`
Extends the `Student` class with:

- `to_json(attrs=None)`
- When `attrs` is a list, only the requested attributes are returned.
- Otherwise, all attributes are returned.

### `11-student.py`
Extends the `Student` class with:

- `to_json(attrs=None)`
- `reload_from_json(json)`

`reload_from_json()` updates the student's attributes from a dictionary.

### `12-pascal_triangle.py`
Creates Pascal's triangle.

- Function: `pascal_triangle(n)`
- Returns `[]` when `n <= 0`.
- Returns a list of lists containing the values of Pascal's triangle.
- Does not import any module.

Example:

```python
pascal_triangle(5)

100-append_after.py

Inserts a line of text after every line containing a specific string.

Function: append_after(filename="", search_string="", new_string="")
Uses the with statement.
Does not import any module.
10-metrics.py

Reads log entries from standard input and calculates running metrics.

It:

Reads input line by line.
Calculates the total file size.
Counts supported HTTP status codes.
Prints statistics every 10 valid lines.
Prints the current statistics when interrupted with CTRL+C.
Prints status codes in ascending order.

Supported status codes:

200
301
400
401
403
404
405
500

Example output:

File size: 5120
200: 7
404: 2
500: 1
Requirements
Python 3
Follow PEP 8 / Pycodestyle conventions where applicable.
No unnecessary module imports.
Use the required function prototypes from each exercise.
Running the Scripts

Make scripts executable when required:

chmod +x filename.py

Run a script:

./filename.py

For scripts that require command-line arguments, provide the required arguments. For example:

./11-main.py student.json
