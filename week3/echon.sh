#!/bin/bash
if test $# -ne 2
then
    echo "Usage: ./echon.sh <number of lines> <string>"  && exit 1
elif ! [[ $1 =~ ^[0-9]+$ ]]
then
    echo "./echon.sh: argument 1 mush be a non-negative" && exit 1
fi

count=0 
while [ $count -lt $1 ]
do 
 echo $2
 count=$(($count + 1))
done