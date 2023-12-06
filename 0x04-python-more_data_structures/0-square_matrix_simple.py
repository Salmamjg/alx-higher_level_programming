#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for x in matrix:
        matrix_row = []
        for element in x:
            matrix_row.append(element ** 2)
        squared_matrix.append(matrix_row)
    return squared_matrix
