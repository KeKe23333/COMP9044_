#!/usr/bin/env python3

import fileinput
import re

total = 0

for line in fileinput.input():

    nums = re.findall('\d+', line)

    if len(nums)  !=  0:
        nums = [int(i) for i in nums]
        total+=sum(nums)

print(total)