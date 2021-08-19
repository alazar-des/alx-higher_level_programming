#!/bin/bash
# display content length
echo $(curl -s --head "$1"  | grep -i Content-Length | awk '{print $2}')
