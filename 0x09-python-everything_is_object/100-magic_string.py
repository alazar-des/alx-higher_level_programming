#!/usr/bin/python3
str = "Holberton"
def magic_string():
    global str; prev = str; str += ', ' + "Holberton"; return prev
