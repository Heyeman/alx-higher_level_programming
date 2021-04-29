#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    x = 0
    for i in range(len(argv) - 1):
        x += int(argv[i + 1])
    print("{:d}".format(x))
