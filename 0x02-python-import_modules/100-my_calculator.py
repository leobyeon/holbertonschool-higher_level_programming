#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    if len(arg) != 4:
        print("{:s}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    else:
        if arg[2] == '+':
            print("{:d} + {:d} = {:d}".format(arg[1], arg[3], add(arg[1], arg[3])))
        elif arg[2] == '-':
            print("{:d} - {:d} = {:d}".format(arg[1], arg[3], sub(arg[1], arg[3])))
        elif arg[2] == '*':
            print("{:d} * {:d} = {:d}".format(arg[1], arg[3], mul(arg[1], arg[3])))
        elif arg[2] == '/':
            print("{:d} / {:d} = {:d}".format(arg[1], arg[3], div(arg[1], arg[3])))
        else:
            print("{:s}".format("Unknown operator. Available operators: +, -, * and /"))
            exit(1)
