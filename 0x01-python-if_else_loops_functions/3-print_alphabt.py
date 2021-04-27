#!/usr/bin/python3
for i in range(26):
    if (i + 97) != 101 and (i + 97) != 113:
        print("{:c}".format(97 + i), end="")
