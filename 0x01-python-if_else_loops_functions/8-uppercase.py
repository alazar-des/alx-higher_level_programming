#!/usr/bin/python3
def uppercase(str):
    """
    Change lowercase letter to uppercase in a string.
    """
    for i in range(len(str)):
        if (ord(str[i]) >= ord('a')) and (ord(str[i]) <= ord('z')):
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print("{}".format(str[i]), end="")
    print()
