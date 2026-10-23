#!/bin/bash
# Send the required request to catch the response
curl -sL -X PUT -H "Origin: School" -d "user_id=98" "$1"
