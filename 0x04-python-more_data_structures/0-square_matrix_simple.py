#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        result.append(list(map(lambda x: x * x, row)))

    return result
