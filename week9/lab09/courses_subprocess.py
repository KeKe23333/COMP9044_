#!/usr/bin/env python3
import sys


import re
import subprocess


arg = sys.argv[1]
web = f"http://www.timetable.unsw.edu.au/2022/{arg}KENS.html"

# print(web)
data = subprocess.run(f"curl --location --silent \"{web}\"", shell=True, capture_output=True, text=True).stdout

# print(data)

courses = re.findall(r'<td class=\"data\"><a href=\"([A-Z]{4}[0-9]{4}).html\">(.*?)</a></td>', data)
#print(courses)

courses = sorted(courses, key = lambda tup: tup[0])


printed = []

# courses = [(1, 2), (2, 3), (3, 4)]

for course in courses:
    if course[0] != course[1] and course[0] not in printed :
        print(course[0] + ' ' + course[1])
        printed.append(course[0])