#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a_list = []
    for index, value in enumerate(my_list):
        if value % 2 == 0:
            a_list[index] = True
        else:
            a_list[index] = False
    return (a_list)
