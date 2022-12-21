#! /usr/bin/env python3

from distutils.filelist import findall
import sys
import re
import csv

data = csv.reader(sys.stdin, delimiter='|')

output = csv.writer(sys.stdout, delimiter='|')

for course, zid, name, num, gender in data :
    name = re.findall(r"^(.*), (.*?)(\s*)$", name)
   # print(name)
    res = name[0][1] + " " + name[0][0]+ name[0][2]
    #print(res)
    output.writerow([course, zid, res, num, gender])

# for course, stuid, name, progam, gender in csv.reader(sys.stdin, delimiter='|'):
#     name = re.fullmatch(r"(.*), (.*?)(\s*)", name)
#     name = name.group(2) + " " + name.group(1) + name.group(3)
#     out.writerow([course, stuid, name, progam, gender])