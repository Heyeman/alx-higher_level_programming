#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) < 123 and ord(i) > 96:
            i = chr(ord(str[i]) - 32)
    print(str)
uppercase("holberton")
uppercase("Holberton School 98 Battery street")
