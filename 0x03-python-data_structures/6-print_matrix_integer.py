#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print elements of matrix.
    """
    for i in range(len(matrix)):
        end = len(matrix[i]) - 1
        for j in range(end):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("{:d}".format(matrix[i][end]))
