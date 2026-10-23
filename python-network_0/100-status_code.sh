#!/bin/bash
# Display the HTTP status code returned by the server
curl -s -o /dev/null -w "%{http_code}" "$1"
