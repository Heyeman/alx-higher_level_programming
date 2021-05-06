#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    my_list = list(set(my_list))
    for y in my_list:
        x += y
    return x
