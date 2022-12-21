#!/usr/bin/env python3

import sys


num = int (sys.argv[1])

lines = []

total = 0 # total number
count = 0

for line in sys.stdin:

    total +=1
    line = line.replace(" ", '')

    line = line.lower()

    if line not in lines:
        lines.append(line)
        count+=1
    if count ==num:
        print(str(count) + ' distinct lines seen after ' + str(total)+  ' lines read')
        break

if count != num:

    print('End of input reached after ' + str(total) + ' read - ' + str(num) + ' different lines not seen')