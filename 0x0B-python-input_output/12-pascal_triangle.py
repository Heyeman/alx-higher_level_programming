#!/usr/bin/python3
"""Return pascal Triangle."""


def pascal_triangle(n):
    """Return pascal Trinagle matrix of n.
    Args:
        n (int): the nth number the pascal triangle to be returned
    Yields:
        matrix of pascal triangle of n.
    """
    pascal_trg = []
    if n <= 0:
        return pascal_trg
    pascal_trg.append([1])
    for i in range(1, n):
        row = []
        row.append(1)
        for j in range(1, i):
            row.append(pascal_trg[i-1][j-1] + pascal_trg[i-1][j])
        row.append(1)
        pascal_trg.append(row)
    return pascal_trg
