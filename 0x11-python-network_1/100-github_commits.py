#!/usr/bin/python3
"""list 10 recent commits from GitHub repository.
"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(sys.argv[2], sys.argv[1]))
    r_json = resp.json()
    for i in range(len(r_json)):
        if i >= 10:
            break
        diction = r_json[i]
        print("{}: {}".format(diction['sha'],
                              diction['commit']['author']['name']))
