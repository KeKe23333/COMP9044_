#!/usr/bin/env python3

import fileinput
import re

pods = {}

nums = {}

types = []

for line in fileinput.input():
    m = re.search(r'\d{2}/\d{2}/\d{2} +?(\d+) (.*)', line)
    num = m.group(1)
    type = m.group(2).lower()
    type = re.sub(' +', ' ', type)
    type = re.sub('^ ', '', type)
    type = re.sub(' $', '', type)
    type = re.sub('s$', '', type)

    if type not in pods.keys():
        types.append(type)
        pods[type]=1
        nums[type]=int(num)
    else:
        pods[type]+=1
        nums[type]+=int(num)

types.sort()
for type in types:
    print(f"{type} observations: {pods[type]} pods, {nums[type]} individuals")
