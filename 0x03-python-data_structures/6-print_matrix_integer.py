#!/usr/bin/python3
def print_matrix_integer(matri=[[]]):
    if len(matri) == 0 or matri is None:
        return (None)
    for i in range(len(matri)):
        for j in range(len(matri[i])):
            if j == len(matri[i]) - 1:
                print("{:d}".format(matri[i][j]))
            else:
                print("{:d}".format(matri[i][j]), end=' ')
