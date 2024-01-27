#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a_list = []
    for i in enumerate(my_list):
        if i % 2 == 0:
            a_list[i] = True
        else:
            a_list[i] = False
    return (a_list)
