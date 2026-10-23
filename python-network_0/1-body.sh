#!/bin/bash
# Sends a GET request to a URL and displays the body only if the status code is 200
response=$(curl -s -w "\n%{http_code}" "$1")
status="${response##*$'\n'}"
body="${response%$'\n'*}"
if [ "$status" -eq 200 ]; then
    echo "$body"
fi
