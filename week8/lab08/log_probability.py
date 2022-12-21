#!/usr/bin/env python3
import glob
import math
import re
import sys

def total_(lines):
    total = 0 

    for line in lines:
        words = re.findall(r'[a-zA-Z]+', line)

        total +=len(words)

    return total

def count_(lines, arg):
    times = 0
    find = r'\b' + arg + r'\b'

    for line in lines:
        sub_times = re.findall(find, line, flags=re.I)
        times+=len(sub_times)

    return times + 1

data = {}

for file in glob.glob("lyrics/*.txt"):
    fp = open(file, 'r')
    lines = fp.readlines()
    fp.close()
    total = total_(lines)
    counts = []
    for arg in sys.argv[1:]:
        counts.append(count_(lines, arg))
    res = 0
    for value in counts:
        log = math.log(value/total)
        res +=log 
    file_name = file.replace('lyrics/', '')
    file_name = file_name.replace('.txt', '')
    file_name = file_name.replace('_', ' ')
    
    data[file_name] = res

for key in sorted(data.keys()):
    print(f'{data[key]:10.5f} {key}')

 