#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared = []
    for line in matrix:
        squared.append([i**2 for i in line])
    return squared
