#!/usr/bin/python3
def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    if n <= 0:
        return []

    outer = []

    for i in range(n):
        if i == 0:
            inner = [1]
            outer.append(inner)
            continue

        if i == 1:
            inner = [1, 1]
            outer.append(inner)
            continue

        inner = [list for list in range(i + 1)]
        for j in range(1, i):
            inner[0] = 1
            inner[i] = 1
            inner[j] = outer[i - 1][j] + outer[i - 1][j - 1]

        outer.append(inner)

    return outer
