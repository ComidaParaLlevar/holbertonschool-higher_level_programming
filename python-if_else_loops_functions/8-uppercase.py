#!/usr/bin/python3
def uppercase(str):
    for i in (len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            diff = 32
        else:
            diff = 0
        print("{:c}".format((ord(str[i]) - diff)), end="")
    print()
