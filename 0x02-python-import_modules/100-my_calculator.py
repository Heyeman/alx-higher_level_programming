#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] != "+" or argv[2] != "-" or argv[2] != "*" or argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == "+":
            print("{:d} {} {:d} = {:d}".format(argv[1], argv[2], argv[3], argv[1] + argv[3]))
        elif argv[2] == "-":
            print("{:d} {} {:d} = {:d}".format(argv[1], argv[2], argv[3], argv[1] - argv[3]))
        elif argv[2] == "*":
            print("{:d} {} {:d} = {:d}".format(argv[1], argv[2], argv[3], argv[1] * argv[3]))
        elif argv[2] == "/":
            print("{:d} {} {:d} = {:d}".format(argv[1], argv[2], argv[3], argv[1] / argv[3])
