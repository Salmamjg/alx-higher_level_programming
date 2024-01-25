#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list: A new matrix where each element is the
        result of dividing the corresponding element
        in the original matrix by the specified number,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return result_matrix
