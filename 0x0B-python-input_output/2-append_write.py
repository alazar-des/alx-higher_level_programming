#!/usr/bin/python3
"""Write to a file"""


def append_write(filename="", text=""):
    """Append to a file. If file doesn't exist will be created with the
    filename name.

    Args:
        filename (str): file name the text to be append to.
        text (str): text to be append

    Yields:
        The number of characters written to the file.
    """
    with open(filename, 'a') as f:
        return f.write(text)
