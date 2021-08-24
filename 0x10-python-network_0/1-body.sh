#!/bin/bash
# sends a request to that URL and displays the size of the body of the response

if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ]
then
    curl -s "$1"
fi
