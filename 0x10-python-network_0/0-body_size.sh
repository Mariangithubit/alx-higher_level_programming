#!/bin/bash
# Display the size of the body of the response URL
curl -s "$1" | wc -c
