#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        c = 1
        l = len(i)
        for j in i:
            if c == l:
                print("{:d}".format(j), end='')
            else:
                print("{:d}".format(j), end=' ')
            c += 1
        print()
