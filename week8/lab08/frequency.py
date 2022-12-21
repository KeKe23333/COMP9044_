#!/usr/bin/env python3
import glob
import re
import sys

def total_(lines):
    total = 0 

    for line in lines:
        words = re.findall(r'[a-zA-Z]+', line)

        total +=len(words)

    return total

def count_(lines):
    times = 0
    arg = sys.argv[1]
    find = r'\b' + arg + r'\b'

    for line in lines:
        sub_times = re.findall(find, line, flags=re.I)
        times+=len(sub_times)

    return times

data = {}

for file in glob.glob("lyrics/*.txt"):
    fp = open(file, 'r')
    lines = fp.readlines()
    fp.close()
    total = total_(lines)
    count = count_(lines)

    file_name = file.replace('lyrics/', '')
    file_name = file_name.replace('.txt', '')
    file_name = file_name.replace('_', ' ')
    
    data[file_name] = (total, count)

for key in sorted(data.keys()):
    print(f'{data[key][1]:4}/{data[key][0]:6} = {data[key][1]/data[key][0]:.9f} {key}')

 