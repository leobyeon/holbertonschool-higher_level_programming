#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    answer = []
    for i in matrix:
        answer.append(list(map(lambda x: x**2, i)))
    return answer
