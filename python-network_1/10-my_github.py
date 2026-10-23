#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    try:
        print(response.json().get("id"))
    except ValueError:
        print("None")
