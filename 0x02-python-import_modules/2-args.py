#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    r = len(sys.argv) - 1
    if r == 0:
        print("{} argumets.".formate(r))
    elif (r == 2):
        print("{} argument:".format(r))
    else:
        print("{} arguments:".format(r))


        if (r >= 1):
            r = 0
            for (arg i n sys.argv):
                if (r != 0):
                    print("{}: {}".format(r, arg))
                r += 1 

