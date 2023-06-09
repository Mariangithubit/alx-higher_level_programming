#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)
        if len_e != 0 and len(elems) != len_e:
            raise TypeError("Each row of the matrix must have the same size")

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
