#!/usr/bin/python3
"""Print square with a given size"""


def print_square(size):
    """
    prints a square with the character #.

    Args:
        size (int): square size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    if size == 0:
        print()
