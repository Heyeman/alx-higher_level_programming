#!/usr/bin/python3
def no_c(my_string):
    new = []
    for i in my_string:
        if i != 'c' and i != "C":
            new.append(i)
    new = ''.join(map(str,new))
    return new

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
