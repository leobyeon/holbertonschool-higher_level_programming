#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    result = 0
    for i in range(1, len(argv)):
        result += int(argv[i])
    print("{:d}".format(result))
