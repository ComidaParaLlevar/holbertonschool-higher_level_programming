#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        counter = 1
        lenght = len(i)
        for j in i:
            if counter == lenght:
                print("{:d}".format(j), end='')
            else:
                print("{:d}".format(j), end=' ')
            counter += 1
        print()
