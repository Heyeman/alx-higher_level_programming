#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        print("{:d}".format(number % 10))
    elif number == 0:
        print("{:d}".format(0))
    else:
        number = -number
        print("{:d}".format(number % 10))
print_last_digit(98)
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
