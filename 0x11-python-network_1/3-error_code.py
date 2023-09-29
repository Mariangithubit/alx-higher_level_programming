#!/usr/bin/python3
""" sends a request to the URL
- print: Error code:
- followed by the HTTP status code
"""
import sys
from urllib import request, error


try:
    with request.urlopen(sys.argv[1]) as sour:
        print(sour.read().decode("utf-8"))
except error.HTTPError:
    print('Error code:', error.HTTPError.code)
