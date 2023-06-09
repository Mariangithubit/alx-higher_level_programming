#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    n = len(arg) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))
    for i in range(n):
        print("{}: {}".format(i + 1, arg[i + 1]))
