#!/usr/bin/python3
"""Uses the GitHub API to display the id of the user with the credentials."""
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
