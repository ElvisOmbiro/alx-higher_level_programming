#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    return ([list(map(lambda p: p * p, row)) for row in matrix])
