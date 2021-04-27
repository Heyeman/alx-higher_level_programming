#!/usr/bin/python3
def uppercase(str):
    for i in str:
<<<<<<< HEAD
        if ord(i) < 123 and ord(i) > 96:
            i = chr(ord(str[i]) - 32)
    print(str)
uppercase("holberton")
uppercase("Holberton School 98 Battery street")
=======
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print("")
>>>>>>> 540b5fca62b234b222602c055b04c5fb87bf2ee6
