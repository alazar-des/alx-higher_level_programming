#!/usr/bin/python3
"""
print request id
"""
import requests
import sys


resp = requests.get(sys.argv[1])
print(resp.headers['X-Request-Id'])
