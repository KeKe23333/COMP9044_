#!/usr/bin/env python3

import sys

input = sys.argv[1]
output = sys.argv[2]



if __name__ =="__main__":
    content = []

    with open (input) as f :
        for row in f.readlines():
            content.append(row)

    content.reverse()
    #print(content)
    with open(output,"w") as o_f:
        for row in content:
            o_f.write(row)
