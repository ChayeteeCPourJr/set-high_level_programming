#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add 2 tuples element-wise, using only their first 2 integers

    Args:
        tuple_a: first tuple of integers
        tuple_b: second tuple of integers

    Returns:
        A tuple with 2 integers: the sum of the first elements of
        tuple_a and tuple_b, and the sum of the second elements.
        Missing elements (if a tuple has fewer than 2 items) are
        treated as 0. Extra elements beyond the first 2 are ignored.
    """
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a0 + b0, a1 + b1)
