#!/bin/dash

i=1
while test $i -le $1

do
    echo "hello $2" > hello${i}.txt
    i=$((i+1))

done 