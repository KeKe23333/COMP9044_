#!/usr/bin/env python3

from urllib import response
import requests
from bs4 import BeautifulSoup
import sys

arg = sys.argv[1]
web = f"http://www.timetable.unsw.edu.au/2022/{arg}KENS.html"

res = requests.get(web).text

soup = BeautifulSoup(res, "html5lib")
soup = soup.find_all('a')

course = {}

curr = ''

for s in soup:
    if s.get("href") != None and arg in s.get("href") and curr != s.get("href"):
        curr = s.get("href")
        course[curr] =  None

    elif s.get("href") != None and curr ==s.get("href"):
        course[curr] = s.get_text()

for key in sorted(course.keys()):
    code = key.replace(".html", '')
    print(code + ' ' + course[key])