#!/usr/bin/env python3

import fileinput
import re


sum = 0

for line in fileinput.input():

    m = re.search (r'\d{2}/\d{2}/\d{2} +?(\d+) (.*)',line)
    # print(m)

    num = m.group(1)
        # print(num)
    type = m.group(2)
                                    # ingnore the  case
    if re.search(r'Orca', type, flags=re.I):
        sum =  sum + int(num)

print(str(sum) + " Orcas reported")