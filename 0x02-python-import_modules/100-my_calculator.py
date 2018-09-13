#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    error1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    error2 = "Unknown operator. Available operators: +, -, * and /"
    if len(arg) != 4:
        print("{:s}".format(error1))
        exit(1)
    else:
        v1 = int(arg[1])
        v2 = int(arg[3])
        op = arg[2]
        if op == '+':
            print("{:d} + {:d} = {:d}".format(v1, v2, add(v1, v2)))
        elif op == '-':
            print("{:d} - {:d} = {:d}".format(v1, v2, sub(v1, v2)))
        elif op == '*':
            print("{:d} * {:d} = {:d}".format(v1, v2, mul(v1, v2)))
        elif op == '/':
            print("{:d} / {:d} = {:d}".format(v1, v2, div(v1, v2)))
        else:
            print("{:s}".format(error2))
            exit(1)
