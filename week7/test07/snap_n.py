#!/usr/bin/env python3
import sys


word = {}
num = int (sys.argv[1])

for line in sys.stdin:
    if line not in word.keys():
        word[line] = 1
    else : 

        word[line]+=1

    if word[line] == num:
        print(f"Snap: {line.strip()}")
        break