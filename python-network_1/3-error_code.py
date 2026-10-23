#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response.

Prints the error code if an HTTPError occurs.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
