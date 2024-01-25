#!/usr/bin/python3
def uppercase(str):
    for i in (len(str)):
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            print("{}".format((ord(str[i]) - 32)), end="")
        else:
            print("{}".format(i), end="")


