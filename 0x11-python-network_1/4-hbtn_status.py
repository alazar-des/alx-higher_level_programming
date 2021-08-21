#!/usr/bin/python3
"""
print status of request response
"""
import requests


resp = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("- type: ", type(resp.text))
print("- content: ", resp.text)
