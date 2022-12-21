#!/usr/bin/env python3
import sys


word = []

for line in sys.argv[1:]:

    if line not in word:
        word.append(line)

print(' '.join(word))