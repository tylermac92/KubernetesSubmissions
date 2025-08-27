#!/usr/bin/env bash

# Infinite loop to print string every 5 seconds with timestamp
while true; do
    RANDOM_STRING=$(openssl rand -base64 12)
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] $RANDOM_STRING"
    sleep 5
done

