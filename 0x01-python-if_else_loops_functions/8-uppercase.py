#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < 123 and ord(str[i]) > 96:
            print("{:c}".format(ord(str[i]) - 32), end="")

uppercase("holberton")
uppercase("Holberton School 98 Battery street")
