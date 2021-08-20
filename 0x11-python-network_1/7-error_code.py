#!/usr/bin/python3
"""
send email post and print response body.
"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if(resp.ok):
        print(resp.text)
    else:
        print("Error code: ", resp.status_code)
