#!/usr/bin/env python3
import sys
import re

match = False

if len(sys.argv) <=1: print('')
else:
    for arg in sys.argv[1:]:
        result = re.search(r'[aeiouAEIOU]{3}', arg)

        if result != None:
            print(arg, end = ' ')
            match = True

    if match: print('')