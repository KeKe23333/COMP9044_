#!/usr/bin/env python3

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
file = sys.argv[3]



if __name__ =="__main__":
    ouput_file=open(file,mode='w+')

    for num in range (start, end+1):
        # if num == end:
        #     ouput_file.write(str(num))
        # else:
        #     ouput_file.write(str(num) + "\n")
        ouput_file.write(str(num) + "\n")
    
    ouput_file.close()
    