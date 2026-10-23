#!/bin/bash
# Displays all HTTP methods the server accepts for a given URL
curl -sI -X OPTIONS "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
