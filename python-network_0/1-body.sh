#!/bin/bash
curl -s "$1" -w "%{http_code}" -o /dev/null
