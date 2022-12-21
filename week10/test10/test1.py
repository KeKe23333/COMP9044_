
#!/usr/bin/env python3
import sys
import re

# test 1
"""
# store the input
lines = []
for line in sys.stdin:
  # common input
  if re.search(r'^#[0-9]+$', line) == None:
    lines.append(line)
  # #[0-9]
  else:
    # 占位
    lines.append(int(line[1:]))

for line in lines:
  if isinstance(line, int):
    print(lines[line-1], end='')
  else:
    print(line, end='')

"""

# test 2

"""
result = []
for line in sys.stdin:
  # 1. get all the numbers
  numbers = re.findall(r'\d+.?\d*', line)
  print(numbers)
  # traverse
  for num in numbers:
    print(str(round(float(num))))
    # replace the substring
    line = line.replace(num, str(round(float(num))))
    result.append(line)

print(''.join(result))
"""

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', "L", 'M', 'N', "O", 'P', 'Q', 'R', 'S', 
'T', 'U', 'V', 'W', 'S', 'Y', 'Z']
try:
  shift = int(sys.argv[1])
except: 
  sys.exit(1)
result = []
# read input
for line in sys.stdin:
  # convert the line in to list
  chars = list(line)
  # traverse
  for i  in range(0, len(chars)):
    # get the current char
    char = chars[i]
    # upper case
    if char in letters:
      # find the index
      index = letters.index(char)
      # shift
      index = index + shift
      # get the mod
      index = index % 26
      # replace
      chars[i] = letters[index]
    # lower case
    elif char.upper() in letters:
      # find the index
      index = letters.index(char.upper())
      # shift
      index = index + shift
      # get the mode
      index = index % 26
      # replace, change to lower
      chars[i] = letters[index].lower()
  # join the list into line
  print(''.join(chars))

