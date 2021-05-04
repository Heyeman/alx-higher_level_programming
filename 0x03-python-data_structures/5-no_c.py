#!/usr/bin/python3
def no_c(my_string):
    new = []
    for i in range(len(my_string)):
        if my_string[i] != "c" or my_string[i] != "C":
            new.append(my_string[i])
    return new

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
