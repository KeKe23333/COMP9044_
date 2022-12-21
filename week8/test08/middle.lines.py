#!/usr/bin/env python3
import sys


file = sys.argv[1]

fp = open(file, 'r')
lines = fp.readlines()
fp.close()

size = len(lines)

if size % 2 == 0:
    index = size/2
    print(lines[int(index)], end = '')
    print(lines[int(index+1)], end = '')

else:
    index = (size-1)/2

    print(lines[int(index)],end = '')
