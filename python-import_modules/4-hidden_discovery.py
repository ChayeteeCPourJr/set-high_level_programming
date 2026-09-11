#!/usr/bin/python3
"""Discovers and prints the names of all functions defined inside a
compiled Python file (.pyc), sorted alphabetically."""
import importlib.util
import marshal


def get_function_names(code, names=None):
    """Recursively collect function/method names from a code object."""
    if names is None:
        names = set()
    for const in code.co_consts:
        if hasattr(const, "co_name"):
            if not const.co_name.startswith("__"):
                names.add(const.co_name)
            get_function_names(const, names)
    return names


def main():
    filename = "hidden_4.pyc"
    header_size = importlib.util.MAGIC_NUMBER.__len__() + 12

    with open(filename, "rb") as f:
        f.read(header_size)
        code = marshal.load(f)

    for name in sorted(get_function_names(code)):
        print(name)


if __name__ == "__main__":
    main()
