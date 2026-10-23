#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": q}
    )

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
