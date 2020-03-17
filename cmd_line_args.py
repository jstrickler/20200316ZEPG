#!/usr/bin/env python
import sys

print(sys.argv)

print("script name:", sys.argv[0])

print("first arg:", sys.argv[1])

print("second arg:", sys.argv[2])

if len(sys.argv) > 1:
    for file_name in sys.argv[1:]:
        # read file here.....
