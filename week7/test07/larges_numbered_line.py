#!/usr/bin/env python3
import sys
import re

num = []
inputs = {}

for line in sys.stdin:

#                       -?\d*.\d+|-?\d+
    result = re.findall(r'-?\d+\.*\d*', line)
    print(result)
    if result:
        output = [float(i) for i in result]

        num.append(max(output))

        if max(output) not in inputs.keys():
            inputs[max(output)] = [line]
        else:
            inputs[max(output)].append(line)

result = ''.join(inputs[max(num)])

print(result, end='')