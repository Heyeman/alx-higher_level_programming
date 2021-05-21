#!/usr/bin/python3
"""Matrix maltiplication.
Input should be non empty lists of list of int or float.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrix and return the result matrix.

    Args:
        m_a (list of list): first input matrix
        m_b (list of list): second input matrix

    Yields:
        list of list
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    row_a = len(m_a)
    column_a = len(m_a[0])
    row_b = len(m_b)
    column_b = len(m_b[0])
    if column_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")
    for row in m_a:
        if len(row) != column_a:
            raise TypeError("each row of m_a must be of the same size")
        for ele in row:
            if type(ele) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if len(row) != column_b:
            raise TypeError("each row of m_b must be of the same size")
        for ele in row:
            if type(ele) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    m = [[0 for m in range(column_b)] for n in range(row_a)]
    for k in range(column_b):
        for i in range(row_a):
            sum = 0
            for j in range(column_b):
                m[i][k] += m_a[i][j] * m_b[j][k]
    return m
