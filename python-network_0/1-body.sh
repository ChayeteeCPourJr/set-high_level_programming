#!/bin/bash
# Display the body only for HTTP status 200
curl -s -w "\n%{http_code}" "$1" | awk 'BEGIN { RS = "\n" } { lines[NR] = $0 } END { status = lines[NR]; if (status == 200) for (i = 1; i < NR; i++) print lines[i] }'
