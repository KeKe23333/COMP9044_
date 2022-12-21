#!/usr/bin/env python3
import sys
import re

file = sys.argv[1]
fp = open(file, 'r')

with open(file,'r') as f:
    lines = f.readlines()
    lines.sort(key=lambda x: len(x))
    for line in lines:
        print (line,end = '')
    f.close()