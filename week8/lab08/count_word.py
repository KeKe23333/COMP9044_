#!/usr/bin/env python3
from pprint import pprint
import sys
import re
time = 0


#word
arg = sys.argv[1]

find = r'\b' + arg + r'\b' # raw string

for line in sys.stdin:
    sub_times = re.findall(find, line, flags= re.I)
    time += len(sub_times)

print(arg + 'occured'+ time + 'times')


