#!/bin/dash

max=0
max_file=''
for file in "$@"
do
    if test `wc -l < $file` -gt $max
    then
        max=`wc -l < $file`
        max_file=$file
    fi
done
echo $max_file