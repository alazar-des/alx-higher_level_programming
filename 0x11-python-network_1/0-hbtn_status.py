#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urlopen(url) as response:
        data = response.read()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode("UTF-8"))
