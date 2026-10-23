#!/bin/bash
# Send a JSON file in a POST request and display the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
