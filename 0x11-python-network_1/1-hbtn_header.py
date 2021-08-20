#!/usr/bin/python3
"""
Python script that prints reques id
"""
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        print(response.info()['X-Request-Id'])
