#!/usr/bin/python3
"""Display id of GitHub using user credentials.
"""
import requests
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    resp = requests.get('https://api.github.com/user', auth=auth)
    if resp.status_code == 200:
        r_json = resp.json()
        print(r_json['id'])
    else:
        print("None")
