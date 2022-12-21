#!/bin/dash
i=10
while test $i -gt 0
do
	echo $i && 
	i=$((i-1))
done |
sort -n |
uniq