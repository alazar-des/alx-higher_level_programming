#!/usr/bin/python3
def fizzbuzz():
    """
    Print numbers from 1 to 100, and if number is multiple of 3 print Fizz
    if multiple of five Buzz and if multiple of 5 and 3 FizzBuzz.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
