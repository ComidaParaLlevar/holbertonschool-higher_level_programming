#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index = 0
    new_list = my_list
    for i in my_list:
        if i == search:
            new_list[index] = replace
            index += 1
    return new_list
