#!/bin/bash
# print options
curl -s "$1" -X OPTIONS -i | grep -i allow
