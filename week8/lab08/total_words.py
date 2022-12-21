import sys
import re

total  = 0

for line in sys.stdin:
    words = re.findall(r'[a-zA-Z]+', line)

    total+=len(words)

print(str(total) + "words")