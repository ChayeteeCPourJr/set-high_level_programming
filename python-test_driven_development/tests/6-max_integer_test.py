#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max at the end of an ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle of an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the first position."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Max strictly in the middle of the list."""
        self.assertEqual(max_integer([1, 2, 9, 3, 4]), 9)

    def test_one_element(self):
        """A list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling with no argument uses the empty default list."""
        self.assertIsNone(max_integer())

    def test_all_negative(self):
        """A list of only negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9, -1]), -1)

    def test_negative_and_positive(self):
        """A list mixing negative and positive numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_duplicate_max(self):
        """The max value appears more than once."""
        self.assertEqual(max_integer([3, 8, 8, 1]), 8)

    def test_all_equal(self):
        """All elements are identical."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_zeros(self):
        """A list of zeros."""
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_floats(self):
        """A list of floats."""
        self.assertEqual(max_integer([1.5, 3.7, 2.2]), 3.7)

    def test_int_and_float_mix(self):
        """A list mixing ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 2, 0.5]), 2.5)

    def test_large_numbers(self):
        """Very large integers."""
        self.assertEqual(max_integer([10 ** 20, 10 ** 30, 10 ** 10]),
                         10 ** 30)

    def test_list_of_strings(self):
        """Strings are comparable, so the lexicographic max is returned."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_tuple(self):
        """A tuple works since it supports len() and indexing."""
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_string_input(self):
        """A string is a sequence of characters."""
        self.assertEqual(max_integer("hello"), "o")

    def test_list_not_modified(self):
        """The input list is left unchanged."""
        data = [3, 1, 2]
        max_integer(data)
        self.assertEqual(data, [3, 1, 2])

    def test_none_raises_typeerror(self):
        """None has no len(), so a TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_raises_typeerror(self):
        """An int has no len(), so a TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_mixed_types_raises_typeerror(self):
        """Comparing a str with an int raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

    def test_list_of_lists(self):
        """Lists are comparable element by element."""
        self.assertEqual(max_integer([[1, 2], [3, 4], [1, 5]]), [3, 4])


if __name__ == '__main__':
    unittest.main()
