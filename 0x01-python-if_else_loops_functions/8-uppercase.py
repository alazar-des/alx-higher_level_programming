#!/usr/bin/python3
def uppercase(str):
    """
    Change lowercase letter to uppercase in a string.
    """
    for i in range(len(str)):
        if (ord(str[i]) >= ord('a')) and (ord(str[i]) <= ord('z')):
            ch = chr(ord(str[i]) - 32)
        else:
            ch = str[i]
        print(ch, end="")
    print()
