#!/bin/bash
# Display the HTTP methods supported by the server
curl -sI -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ' ' -f 2- | tr -d '\r'
