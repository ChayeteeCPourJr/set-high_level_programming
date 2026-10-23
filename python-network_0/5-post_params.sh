#!/bin/bash
# Send a POST request with email and subject parameters
curl -s -X POST -d "email=test@gmail.com&subject=Hello" "$1"
