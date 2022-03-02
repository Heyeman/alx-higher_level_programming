#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for i in range(len(str)):
        if i == n:
            str1 = str1 + ""
        else:
            str1 = str1 + str[i]
    return str1