#!/usr/bin/env python3

import sys

n= int(sys.argv[1])
input = sys.argv[2]



if __name__ =="__main__":

    #Open the file
    file = open(input,mode='r+')

        #Iterate through lines
    for i, line in enumerate(file):
        if i+1 == n : print(line, end = '')

    #Close the file when you're done
    file.close()
        