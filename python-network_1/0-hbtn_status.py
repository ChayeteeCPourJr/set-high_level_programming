#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and displays the body."""
import urllib.error
import urllib.request


def fetch(url):
    """Return the body of the response from url as bytes."""
    with urllib.request.urlopen(url) as response:
        return response.read()


if __name__ == "__main__":
    try:
        body = fetch('https://alx-intranet.hbtn.io/status')
    except urllib.error.URLError:
        body = fetch('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
