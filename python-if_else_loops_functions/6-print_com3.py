#!/usr/bin/python3
for i in range(0, 10):
    for c in range(i+1, 10):
        if (i == 8) and (c == 9):
            print("{}{}".format(i, c))
        else:
            print("{}{}, ".format(i, c), end="")
