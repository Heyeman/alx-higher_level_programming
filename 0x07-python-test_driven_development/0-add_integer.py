#!/usr/bin/python3
"""
A module contains a function that adds two integers.
The function can accept integer or float input otherwise raise TypeError.
"""


def add_integer(a, b=98):
    """
    Return the addition of two numbers.

    Args:
        a (int or float): The first integer
        b (int or float): The second input integer

    Yields:
        int: the sum of the two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
