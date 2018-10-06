#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function divides a matrix"""
    rowlen = len(matrix[0])
    new = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        innernew = []
        if rowlen is not len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            print(j)
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            innernew.append(round(j / div, 2))
        new.append(innernew)
    return new
