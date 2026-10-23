#!/bin/bash
# Send a request to the specified URL and display the response
curl -sL -X PUT -H "Origin: School" -d "user_id=98" "$1"
