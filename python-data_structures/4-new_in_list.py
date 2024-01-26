#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cp = my_list.copy()
    if idx >= 0 and idx < len(list_cp):
        list_cp[idx] = element

    return list_cp
