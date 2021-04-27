#!/usr/bin/python3
def print_last_digit(number):
    """
    Print last digit of a number and return it.
    """
    if number < 0:
        number = -number
    reminder = number % 10
    print(reminder, end="")
    return reminder
