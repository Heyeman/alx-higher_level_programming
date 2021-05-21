#!/usr/bin/python3
"""print two new line after ., ?, and : characters"""


def text_indentation(text):
    """
    print two new line after ., ?, and : characters.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    b = False
    for i in range(len(text)):
        if b and text[i] == ' ':
            continue
        else:
            print(text[i], end="")
            b = False
        if text[i] in ['.', '?', ':']:
            print()
            print()
            b = True
