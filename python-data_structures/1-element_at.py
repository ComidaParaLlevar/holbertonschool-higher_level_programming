#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    count = len(my_list)
    if idx > count:
        return
    return (my_list[idx], count)
