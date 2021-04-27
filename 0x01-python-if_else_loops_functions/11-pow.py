#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    else:
        x = 1
        if b > 0:
            for i in range(b):
                x = x * a
            return x
        else:
            for i in range(-b):
                x = x / a;
            return x
