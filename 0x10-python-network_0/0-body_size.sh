#!/bin/bash
# display content length

header=$(curl -s --head "$1"  | grep -i Content-Length | awk '{print $2}')
echo "${header}"
