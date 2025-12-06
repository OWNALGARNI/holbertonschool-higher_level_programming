#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and return a new matrix.

    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float) used to divide matrix elements

    Returns:
        A new matrix with all values divided and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a matrix of ints/floats,
                   if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """

    # Validate matrix structure
    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check each element and row size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix (rounded to 2 decimals)
    return [[round(element / div, 2) for element in row] for row in matrix]
