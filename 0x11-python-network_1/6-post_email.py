#!/usr/bin/python3
"""
send email post and print response body.
"""
import requests
import sys


if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    resp = requests.post(sys.argv[1], data=payload)
    print(resp.text)
