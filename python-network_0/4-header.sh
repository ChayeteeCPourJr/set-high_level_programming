#!/bin/bash
# Send a request with a custom header to validate the route
curl -s -H "X-School-User-Id: 98" "$1"
