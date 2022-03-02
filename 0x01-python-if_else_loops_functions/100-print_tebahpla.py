#!/usr/bin/python3
for i in range(25, -1, -1):
    tup = (0, 32)
    m = i % 2
    l = chr(i + 65 + tup[m])
    print("{:s}".format(l), end='')