#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    new_matrix = []
    for i in matrix:
        if matrix:
            new_matrix = (list(map(lambda x: x**2, i)))
    return new_matrix
