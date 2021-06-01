#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Write to a file. If file doesn't exist will be created with the filename
    name.

    Args:
        filename (str): file name the text to be written to.
        text (str): text to be written

    Yields:
        The number of characters written to the file.
    """
    with open(filename, 'w') as f:
        return f.write(text)
