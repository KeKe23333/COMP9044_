#! /usr/bin/env python3
import csv
import sys
import re
import fileinput

sum = 0

for line in fileinput.input():

    m = re.search(r'3711/', line)
    if m != None:
        sum +=1
print(sum, end= '')
    


# sum = 0

# data = csv.reader(sys.stdin, delimiter= '|')

# for course, num, name, program, gender in  data:
#     a, b = program.split('/')

#     if a =='3711':
#         sum +=1

# print(sum)