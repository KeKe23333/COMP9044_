#!/usr/bin/env python3

import re
import sys

pat = sys.argv[1]
file = sys.argv[2]

with open(file, 'r') as fp:
    lines = fp.readlines()

    for line in lines:
        matched = re.search(r'{}'.format(pat), line)

        if matched is not None:
            print(matched.group(),end = '\n')
