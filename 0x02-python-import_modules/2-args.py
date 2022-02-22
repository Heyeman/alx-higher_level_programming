#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
	if len(argv) == 2:
		print("1 argument:")
		print("1: {:s}".format(argv[1]))
	else:
		print("{:d} arguments:".format(len(argv)-1))
		for i in range(len(argv[1:])):
			print("{:d}: {:s}".format(i+1,argv[i+1]))









"""
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{:d} arguments".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {:s}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(len(sys.argv) - 1):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
"""