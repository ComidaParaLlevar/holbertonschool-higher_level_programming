#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if (last > 5):
    print(f"Last digit of {number} is {last} and is greater than 5", end="\n")
elif (last == 0):
    print(f"Last digit of {number} is {last} and is 0", end="\n")
else:
    print(f"Last digit of {number} is {last} and is is less than 6 and not 0", end="\n")
