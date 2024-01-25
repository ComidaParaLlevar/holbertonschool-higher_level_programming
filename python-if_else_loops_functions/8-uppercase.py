#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        if ord(i) >= 97 and ord(i) <= 122:
            diff = 32
        else:
            diff = 0
        print("{}".format(ord(i) - diff), end="")
    print("")
