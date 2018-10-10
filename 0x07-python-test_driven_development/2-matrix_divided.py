#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function divides a matrix"""
    rowlen = len(matrix[0])
    new = []

    if ((type(matrix) is not list) or
        (not all(type(row) is list for row in matrix)) or
        (not all(
        type(i) in (float, int) for row in matrix for i in row))):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        innernew = []
        if rowlen is not len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            innernew.append(round(j / div, 2))
        new.append(innernew)
    return new
