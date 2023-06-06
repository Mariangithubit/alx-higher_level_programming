#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{0:d} is positive".formate(number))
elif number == 0:
    print("{0:d} is zero".formate(number))
else:
    print("{0:d} is negative".formate(number))
