#!/usr/bin/python3
"""
Contains a funciton that divide a matrix elements by a constant number.
Return a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a scalar nubmer and return a new matrix.

    Args:
        matrix (list): a matrix to be divided by div
        div (int): denomnator

    Yields:
        list: a matrix
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row: list(map(lambda x:
                                         round(x / div, 2), row)), matrix))
