#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i[j]**2 for i in matrix] for j in range(0, len(matrix))]
