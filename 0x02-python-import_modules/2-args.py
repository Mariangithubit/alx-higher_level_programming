#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    n = len(arg) - 1


    if n > 1:
        print("{} arguments:".format(n))
        for i in range(1, n + 1):
            print("{}: {}".format(i, arg[i]))
    elif n == 0:
        print("{} argumets.".format(n))
    else:
        print("{} argument:".format(n))
        print("{}: {}".format(n, arg[1]))
