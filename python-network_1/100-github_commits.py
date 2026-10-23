#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository."""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url, params={'per_page': 10})
    for commit in r.json():
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
